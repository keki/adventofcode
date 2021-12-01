import scala.annotation.tailrec
import scala.io.Source

sealed trait Mode
case object Position extends Mode
case object Immediate extends Mode

object Mode {
  def apply(i: Int): Mode = i match {
      case 0 => Position
      case 1 => Immediate
    }
}

sealed trait Instruction {
  val length: Int
  def run(in: List[Int], pos: Int): (List[Int], Int, Option[Int])
}

final case class Add(arg1: Int, arg2: Int, target: Int, mode1: Mode, mode2: Mode) extends Instruction {
  val length = 4
  override def run(in: List[Int], pos: Int): (List[Int], Int, Option[Int]) = {
    val a1 = mode1 match {
      case Position => in(arg1)
      case Immediate => arg1
    }
    val a2 = mode2 match {
      case Position => in(arg2)
      case Immediate => arg2
    }
    (in.updated(target, a1 + a2), pos + length, None)
  }
}

final case class Multiply(arg1: Int, arg2: Int, target: Int, mode1: Mode, mode2: Mode) extends Instruction {
  val length = 4
  override def run(in: List[Int], pos: Int): (List[Int], Int, Option[Int]) = {
    val a1 = mode1 match {
      case Position => in(arg1)
      case Immediate => arg1
    }
    val a2 = mode2 match {
      case Position => in(arg2)
      case Immediate => arg2
    }
    (in.updated(target, a1 * a2), pos + length, None)
  }
}

final case class Input(target: Int, inputParam: Int) extends Instruction {
  val length = 2
  override def run(in: List[Int], pos: Int): (List[Int], Int, Option[Int]) = {
    (in.updated(target, inputParam), pos + length, None)
  }
}

final case class Output(arg: Int, mode: Mode) extends Instruction {
  val length = 2
  override def run(in: List[Int], pos: Int): (List[Int], Int, Option[Int]) = {
    val a = mode match {
      case Position => in(arg)
      case Immediate => arg
    }
    (in, pos + length, Some(a))
  }
}

final case class JumpIfTrue(arg1: Int, arg2: Int, mode1: Mode, mode2: Mode) extends Instruction {
  val length = 3
  override def run(in: List[Int], pos: Int): (List[Int], Int, Option[Int]) = {
    val a1 = mode1 match {
      case Position => in(arg1)
      case Immediate => arg1
    }
    val a2 = mode2 match {
      case Position => in(arg2)
      case Immediate => arg2
    }
    if (a1 != 0) {
      (in, a2, None)
    } else {
      (in, pos + length, None)
    }
  }
}

final case class JumpIfFalse(arg1: Int, arg2: Int, mode1: Mode, mode2: Mode) extends Instruction {
  val length = 3
  override def run(in: List[Int], pos: Int): (List[Int], Int, Option[Int]) = {
    val a1 = mode1 match {
      case Position => in(arg1)
      case Immediate => arg1
    }
    val a2 = mode2 match {
      case Position => in(arg2)
      case Immediate => arg2
    }
    if (a1 == 0) {
      (in, a2, None)
    } else {
      (in, pos + length, None)
    }
  }
}

final case class LessThan(arg1: Int, arg2: Int, target: Int, mode1: Mode, mode2: Mode) extends Instruction {
  val length = 4
  override def run(in: List[Int], pos: Int): (List[Int], Int, Option[Int]) = {
    val a1 = mode1 match {
      case Position => in(arg1)
      case Immediate => arg1
    }
    val a2 = mode2 match {
      case Position => in(arg2)
      case Immediate => arg2
    }
    if (a1 < a2) {
      (in.updated(target, 1), pos + length, None)
    } else {
      (in.updated(target, 0), pos + length, None)
    }
  }
}

final case class Equals(arg1: Int, arg2: Int, target: Int, mode1: Mode, mode2: Mode) extends Instruction {
  val length = 4
  override def run(in: List[Int], pos: Int): (List[Int], Int, Option[Int]) = {
    val a1 = mode1 match {
      case Position => in(arg1)
      case Immediate => arg1
    }
    val a2 = mode2 match {
      case Position => in(arg2)
      case Immediate => arg2
    }
    if (a1 == a2) {
      (in.updated(target, 1), pos + length, None)
    } else {
      (in.updated(target, 0), pos + length, None)
    }
  }
}

case object Halt extends Instruction {
  val length = 1
  override def run(in: List[Int], pos: Int): (List[Int], Int, Option[Int]) = (in, pos + length, None)
}

object Instruction {

  def at(pos: Int, in: List[Int], inputParam: Int): Instruction = {
    val code = in(pos).toString.reverse.padTo(5, '0').reverse;
    val instructionCode = code.takeRight(2).toInt
    val mode1 = code(2).toString.toInt
    val mode2 = code(1).toString.toInt
    val instruction = instructionCode match {
      case 1 => Add(in(pos+1), in(pos+2), in(pos+3), Mode(mode1), Mode(mode2))
      case 2 => Multiply(in(pos+1), in(pos+2), in(pos+3), Mode(mode1), Mode(mode2))
      case 3 => Input(in(pos+1), inputParam)
      case 4 => Output(in(pos+1), Mode(mode1))
      case 5 => JumpIfTrue(in(pos+1), in(pos+2), Mode(mode1), Mode(mode2))
      case 6 => JumpIfFalse(in(pos+1), in(pos+2), Mode(mode1), Mode(mode2))
      case 7 => LessThan(in(pos+1), in(pos+2), in(pos+3), Mode(mode1), Mode(mode2))
      case 8 => Equals(in(pos+1), in(pos+2), in(pos+3), Mode(mode1), Mode(mode2))
      case 99 => Halt
    }
    // println(instruction)
    instruction
  }

}

def run(in: List[Int], inputParams: List[Int]): (List[Int], Int) = {

  def _runAt(pos:Int, in: List[Int], inputParams: List[Int], output: Option[Int]): (List[Int], Option[Int]) = {
    Instruction.at(pos, in, inputParams.head) match {
      case Halt =>
          (in, output)
      case i @ Input(_, _) =>
          val (result, nextPos, outputOpt) = i.run(in, pos)
          _runAt(nextPos, result, inputParams.tail, output.orElse(outputOpt))
      case i =>
          val (result, nextPos, outputOpt) = i.run(in, pos)
          _runAt(nextPos, result, inputParams, output.orElse(outputOpt))
    }
  }

  val (parsedInput, outputOpt) = _runAt(0, in, inputParams, None)
  (parsedInput, outputOpt.get)
}

//input url: https://adventofcode.com/2019/day/7/input
val input: List[Int] =
                Source.fromFile("input.txt").getLines.toList.head.split(',').toList.map(_.toInt)

val phaseSettings = List(0, 1, 2, 3, 4)

val result =
  phaseSettings.permutations.foldLeft(0){ (best, phases) =>
    print(phases)
    val newOutput = phases.foldLeft(0){ (previousOutput, phaseInput) =>
      val (parsedInput, output) = run(input, List(phaseInput, previousOutput, -1))
      print(s" $output")
      output
    }
    if (newOutput > best) {
      println(s" => $newOutput *")
      newOutput
    } else {
      println(s" => $newOutput")
      best
    }
  }

println(s"BEST: $result")

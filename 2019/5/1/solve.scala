import scala.annotation.tailrec
import scala.io.Source


//input url: https://adventofcode.com/2019/day/2/input
val input: List[Int] =
                Source.fromFile("input.txt").getLines.toList.head.split(',').toList.map(_.toInt)

//input parameter
val inputParameter = 1

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
  def run(in: List[Int]): List[Int]
}

final case class Add(arg1: Int, arg2: Int, target: Int, mode1: Mode, mode2: Mode) extends Instruction {
  val length = 4
  def run(in: List[Int]): List[Int] = {
    val a1 = mode1 match {
      case Position => in(arg1)
      case Immediate => arg1
    }
    val a2 = mode2 match {
      case Position => in(arg2)
      case Immediate => arg2
    }
    in.updated(target, a1 + a2)
  }
}

final case class Multiply(arg1: Int, arg2: Int, target: Int, mode1: Mode, mode2: Mode) extends Instruction {
  val length = 4
  def run(in: List[Int]): List[Int] = {
    val a1 = mode1 match {
      case Position => in(arg1)
      case Immediate => arg1
    }
    val a2 = mode2 match {
      case Position => in(arg2)
      case Immediate => arg2
    }
    in.updated(target, a1 * a2)
  }
}

final case class Input(target: Int, inputParam: Int) extends Instruction {
  val length = 2
  def run(in: List[Int]): List[Int] = {
    in.updated(target, inputParam)
  }
}

final case class Output(arg: Int, mode: Mode) extends Instruction {
  val length = 2
  def run(in: List[Int]): List[Int] = {
    val a = mode match {
      case Position => in(arg)
      case Immediate => arg
    }
    println(s"OUTPUT: $a")
    in
  }
}

/*
Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
*/


case object Halt extends Instruction {
  val length = 1
  def run(in: List[Int]): List[Int] = in
}

def instructionAt(pos: Int, in: List[Int], inputParam: Int): Instruction = {
    val code = in(pos).toString.reverse.padTo(5, '0').reverse;
    val instructionCode = code.takeRight(2).toInt
    val mode1 = code(2).toString.toInt
    val mode2 = code(1).toString.toInt
    instructionCode match {
      case 1 => Add(in(pos+1), in(pos+2), in(pos+3), Mode(mode1), Mode(mode2))
      case 2 => Multiply(in(pos+1), in(pos+2), in(pos+3), Mode(mode1), Mode(mode2))
      case 3 => Input(in(pos+1), inputParam)
      case 4 => Output(in(pos+1), Mode(mode1))
      case 99 => Halt
    }
  }

def run(in: List[Int], inputParam: Int): List[Int] = {

  def _runAt(pos:Int, in: List[Int], inputParam: Int): List[Int] = {
    val instruction = instructionAt(pos, in, inputParam)
    val nextPos = pos + instruction.length
      instruction match {
        case Halt =>
            in
        case i =>
            val result = i.run(in)
//            println(result.take(20))
            _runAt(nextPos, result, inputParam)
      }
  }

  _runAt(0, in, inputParam)
}

val result = run(input, inputParameter)

println(result)

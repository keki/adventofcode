import scala.io.Source

sealed trait Command {
	def execute(in: List[Int]): List[Int]
}

case class Add(pos1: Int, pos2: Int, target: Int) extends Command {
	def execute(in: List[Int]): List[Int] = in.updated(target, in(pos1) + in(pos2))
}

case class Multiply(pos1: Int, pos2: Int, target: Int) extends Command {
	def execute(in: List[Int]): List[Int] = in.updated(target, in(pos1) * in(pos2))
}

case object EOF extends Command {
	override def execute(in: List[Int]): List[Int] = in
}

object Command {
	def apply(input: List[Int]): Command =
		input match {
			case List( 1, pos1, pos2, target)  => Add(pos1, pos2, target)
			case List( 2, pos1, pos2, target)  => Multiply(pos1, pos2, target)
			case List(99) => EOF
			case _ => EOF
		}
}

def computeAt(pos: Int, in: List[Int]): List[Int] = {
	if (in.length >= pos + 4) {
		computeAt(pos + 4, Command(in.drop(pos).take(4)).execute(in))
	} else {
		in
	}
}

def compute: List[Int] = {
	//input url: https://adventofcode.com/2019/day/2/input
	val input: List[Int] =
		Source.fromFile("input.txt").getLines.toList.head.split(',').toList.map(_.toInt)
			.updated(1, 12)
			.updated(2, 2)

	computeAt(0, input)
}

val result = compute

println(compute.head)

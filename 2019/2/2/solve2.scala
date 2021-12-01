import scala.annotation.tailrec
import scala.io.Source

//input url: https://adventofcode.com/2019/day/2/input
val input: List[Int] = Source.fromFile("input.txt").getLines.toList.head.split(',').toList.map(_.toInt)

val target = 19690720

def compute(in: List[Int]): Option[Int] = {

	def blockAt(pos: Int, in: List[Int]): List[Int] = in.drop(pos).take(4)

	def exec(block: List[Int], in: List[Int]): List[Int] =
		block match {
			case List( 1, pos1, pos2, target)  => in.updated(target, in(pos1) + in(pos2))
			case List( 2, pos1, pos2, target)  => in.updated(target, in(pos1) * in(pos2))
		}

	@tailrec
	def computeAt(pos: Int, in: List[Int]): List[Int] =
		blockAt(pos, in) match {
			case 99 :: _ => in
			case block => computeAt(pos + 4, exec(block, in))
		}

	computeAt(0, in).headOption
}

def computeWithArgs(arg1: Int, arg2: Int, in: List[Int]): Option[Int] =
	compute(in.updated(1, arg1).updated(2, arg2))

((0 until 99).foldLeft[Option[(Int, Int)]](None) {
	case (None, i) =>
		(0 until 99).foldLeft[Option[(Int, Int)]](None) {
			case (None, j) =>
				computeWithArgs(i, j, input)
					.flatMap(r => Option.when(r == target)((i, j)))
			case (ss, _) => ss
		}
	case (s, _) => s
}) match {
	case None => println("NO SOLUTION :(")
	case Some((noun, verb)) => println(100 * noun + verb)
}

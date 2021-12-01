import scala.annotation.tailrec
import scala.io.Source

//input url: https://adventofcode.com/2019/day/2/input
val input: List[Int] =
		Source.fromFile("input.txt").getLines.toList.head.split(',').toList.map(_.toInt)
			.updated(1, 12)
			.updated(2, 2)

def blockAt(in: List[Int], pos: Int): List[Int] = in.drop(pos).take(4)

def exec(block: List[Int], in: List[Int]): List[Int] =
	block match {
		case List( 1, pos1, pos2, target)  => in.updated(target, in(pos1) + in(pos2))
		case List( 2, pos1, pos2, target)  => in.updated(target, in(pos1) * in(pos2))
	}

def compute(in: List[Int]): List[Int] = {

	@tailrec
	def computeAt(pos: Int, in: List[Int]): List[Int] =
		blockAt(in, pos) match {
			case 99 :: _ => in
			case block => computeAt(pos + 4, exec(block, in))
		}

	computeAt(0, in)
}

val result = compute(input)

println(result.head)

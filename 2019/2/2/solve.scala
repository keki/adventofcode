import scala.annotation.tailrec
import scala.io.Source


//input url: https://adventofcode.com/2019/day/2/input
val input: List[Int] =
		Source.fromFile("input.txt").getLines.toList.head.split(',').toList.map(_.toInt)

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

def computeWithArgs(arg1: Int, arg2: Int, in: List[Int]): List[Int] = {
	val inputWithArguments = in.updated(1, arg1).updated(2, arg2)
	compute(inputWithArguments)
}

var found = false

val target = 19690720

//ugh, kicsit nemfunkcionalisprogramozas itt, de leszarom
val (noun, verb) =
	(for {
		i <- (0 until 99).toList
		j <- (0 until 99).toList
		if !found
	} yield {
		if (computeWithArgs(i, j, input).head == target) {
			found = true
			println(i + "," + j + " FOUND!")
			List((i, j))
		} else {
			println(i + "," + j)
			Nil
		}
	}).flatten.head

println(100 * noun + verb);

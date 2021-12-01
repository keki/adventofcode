import scala.io.Source

//input url: https://adventofcode.com/2019/day/1/input
val result =
	Source.fromFile("input.txt").getLines.foldLeft(0){(acc, line) =>
 		acc + (Math.floor(line.toInt / 3) - 2).toInt
	}

println(result)

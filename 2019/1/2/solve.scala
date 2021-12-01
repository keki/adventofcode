import scala.io.Source

def fuelRequired(mass: Int): Int = {
	val fuel = (Math.floor(mass / 3) - 2).toInt
	if(fuel <= 0) {
		0
	} else {
		fuel  + fuelRequired(fuel)
	}
}

//input url: https://adventofcode.com/2019/day/1/input
val result =
	Source.fromFile("input.txt").getLines.foldLeft(0){(acc, mass) =>
 		acc + fuelRequired(mass.toInt)
	}

println(result)

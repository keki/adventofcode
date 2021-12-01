import scala.io.Source
import scala.annotation.tailrec

//input url: https://adventofcode.com/2019/day/3/input
val input: List[List[String]] =
	Source.fromFile("input.txt").getLines.toList.map(_.split(',').toList)

// "R56" -> Section('R', 56)
final case class Section(direction: Char, steps: Int) {
	override def toString: String = s"$direction$steps"
}

object Section {
	def fromString(str: String): Section = Section(str.head, str.tail.toInt)
}

// "R56,D14" -> List(Section('R', 56), Section('D', 14))
type TurtlePath = List[Section]

// x:y coordinates
final case class Coordinate(x: Int, y: Int) {

	override def toString: String = s"$x:$y"

	def neighbor(direction: Char): Coordinate = {
		direction match {
			case 'R' => this.copy(x = x + 1)
			case 'L' => this.copy(x = x - 1)
			case 'U' => this.copy(y = y + 1)
			case 'D' => this.copy(y = y - 1)
		}
	}

	def manhattanDistance: Int = x + y
}

// just a list of x:y coordinates
type Path = List[Coordinate]

def pathFromTurtle(turtle: TurtlePath): Path = {

	//for performance reasons, we calculate paths in reverse (prepend is fast, append is slow)
	@tailrec
	def _addSection(coordinates: Path, section: Section): Path = {
		if (section.steps > 0) {
			val newCoordinates = coordinates.headOption.getOrElse(Coordinate(0,0)).neighbor(section.direction) +: coordinates
			val remainingSection = section.copy(steps = section.steps - 1)
			_addSection(newCoordinates, remainingSection)
		} else {
			coordinates
		}
	}

	val coords =
		turtle.foldLeft[Path](Nil)((path, section) => _addSection(path, section))

	coords.reverse
}

val turtlePaths = input.map(_.map(Section.fromString))

val paths = turtlePaths.map(pathFromTurtle)

val intersections = paths.foldLeft(List[Coordinate]()) { (acc, path) =>
	if (acc.isEmpty) {
		path
	} else {
		acc.intersect(path)
	}
}

val intersectionsWithDistances =
	intersections map { coordinate =>
		val distances = paths.map(_.indexOf(coordinate) + 1) //index starts with 0
		(coordinate, distances, distances.sum)
	}

val orderedIntersections = intersectionsWithDistances.sortWith((a, b) => a._3 <= b._3)

val closest = orderedIntersections.head

println(closest)



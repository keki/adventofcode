import scala.annotation.tailrec
import scala.io.Source


case class Orbit(center: String, orbiter: String)

case class OrbitWithPath(orbit: Orbit, path: List[String])

//input url: https://adventofcode.com/2019/day/2/input
val input: Set[Orbit] =
                Source.fromFile("input.txt").getLines.toSet
                  .map { line: String =>
                    val items = line.split(')').toSet
                    Orbit(items.head, items.tail.head)
                  }

val starters: Set[OrbitWithPath] = input.filter(_.center == "COM").map(o => OrbitWithPath(o, List(o.orbiter)))

println(starters)

def orbitersOf(orbit: OrbitWithPath, orbits: Set[Orbit]): Set[OrbitWithPath] = orbits.collect {
  case o: Orbit if o.center == orbit.orbit.orbiter => OrbitWithPath(o, orbit.path :+ o.orbiter)
}

def orbitersOfMany(collected: Set[OrbitWithPath], remaining: Set[Orbit]): Set[OrbitWithPath] = collected.flatMap(owp => orbitersOf(owp, remaining))

def exclude(from: Set[Orbit], items: Set[OrbitWithPath]): Set[Orbit] =
  items.foldLeft(from) { (acc, o) => acc - o.orbit }

def allorbits(starters: Set[OrbitWithPath], all: Set[Orbit]): Set[OrbitWithPath] = {

  def _addMore(collected: Set[OrbitWithPath], remaining: Set[Orbit]): Set[OrbitWithPath] = {
    if (remaining.isEmpty) {
      collected
    } else {
      val newOrbits = orbitersOfMany(collected, remaining)
      val furtherRemaining = exclude(remaining, newOrbits)
      _addMore(collected ++ newOrbits, furtherRemaining)
    }
  }

  _addMore(starters, all)
}

def orbitsWithoutStarters = exclude(input, starters)

def result = allorbits(starters, orbitsWithoutStarters)

val orbitcount = result.foldLeft(0)((acc, orbit) => acc + orbit.path.size)

println(result.size)
println(orbitcount)

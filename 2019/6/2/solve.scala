import scala.annotation.tailrec
import scala.io.Source

println("GO!")

case class Orbit(center: String, orbiter: String)

case class Planet(name: String, path: List[String])


//nem tailrec! :(
def orbitersOf(planet: Planet, orbits: Set[Orbit]): Set[Planet] = {
  val directOrbits = orbits.filter(_.center == planet.name)
  val directOrbiters = directOrbits.map(o => Planet(o.orbiter, planet.path :+ o.center))
  val remaining = orbits -- directOrbits
  directOrbiters ++ directOrbiters.flatMap { p =>
    orbitersOf(p, remaining)
  }
}

//input url: https://adventofcode.com/2019/day/2/input
val input: Set[Orbit] =
                Source.fromFile("input.txt").getLines.toSet
                  .map { line: String =>
                    val items = line.split(')').toSet
                    Orbit(items.head, items.tail.head)
                  }

val comOrbit = input.filter(_.center == "COM").toList.head

val com = Planet(comOrbit.orbiter, List(comOrbit.center))

val orbitTree = orbitersOf(com, input - comOrbit)

val san = orbitTree.find(_.name == "SAN").get
println(s"SAN: ${san.path.head} .. ${san.path.last}, ${san.path.size}")

val you = orbitTree.find(_.name == "YOU").get
println(s"YOU: ${you.path.head} .. ${you.path.last}, ${you.path.size}")

val commonPath = you.path.zip(san.path).takeWhile(i => i._1 == i._2).map(_._1)
println(s"COMMONPATH: ${commonPath.head} .. ${commonPath.last}, ${commonPath.size}")

val result = san.path.size + you.path.size - (commonPath.size * 2)
println(s"$result")


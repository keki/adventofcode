object Solve {

	type Digits = List[List[Int]]

	def main(args: Array[String]): Unit = {

		val lines: List[String] = scala.io.Source.fromFile("input").getLines().toList
		val digits: Digits = lines.map(line => line.map(char => char.asDigit).toList)

		def mostCommonBit(d: Digits, pos: Int): Int =
			Math.round(d.map(_(pos)).sum.toFloat / d.size)

		def leastCommonBit(d: Digits, pos: Int): Int =
			1 - mostCommonBit(d, pos)

		def digitsToInt(n: List[Int]): Int =
			Integer.parseInt(n.mkString(""), 2)

		def rating(d: Digits, f: (Digits, Int) => Int): Int = {

			def findRating(d: Digits, pos: Int): Digits =
				// list.size is expensive in scala, so we check if we have finished this way
				if (d.tail.isEmpty) {
					d
				} else {
					val bit_value_at_pos = f(d, pos)
					val matches = d.filter(_(pos) == bit_value_at_pos)
					findRating(matches, pos + 1)
				}

			val ratingAsDigits = findRating(d, 0).head
			digitsToInt(ratingAsDigits)
		}

		val oxygenGeneratorRating = rating(digits, mostCommonBit)
		val co2GeneratorRating = rating(digits, leastCommonBit)

		println(oxygenGeneratorRating * co2GeneratorRating)
	}
}





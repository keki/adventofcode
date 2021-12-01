val from = 171309
val to = 643603

def toDigits(i: Int): Seq[Int] = i.toString.map(_.toString.toInt)

case class PartialResult(hasDouble: Boolean, currentStreak: Int, prevDigit: Int)

def hasDoubleDigitNoTriplet(i: Int): Boolean = {
	val result =
		toDigits(i).foldLeft(PartialResult(false, 0, -1)){ (acc, digit) =>


			if (acc.currentStreak == 0) {
				//just started
				acc.copy(currentStreak = 1, prevDigit = digit)
			} else if (acc.currentStreak == 1) {
				//no multiple digit matching until previous position
				if (acc.prevDigit == digit) {
					acc.copy(currentStreak = 2)
				} else {
					acc.copy(currentStreak = 1, prevDigit = digit)
				}
			} else if (acc.currentStreak == 2) {
				//double at previous position
				if (acc.prevDigit == digit) {
					acc.copy(currentStreak = 3)
				} else {
					acc.copy(true, currentStreak = 1, prevDigit = digit)
				}
			} else {
				//triplet or longer at previous position
				if (acc.prevDigit == digit) {
					acc.copy(currentStreak = acc.currentStreak + 1)
				} else {
					acc.copy(currentStreak = 1, prevDigit = digit)
				}
			}
		}

	//has to account for the case when the last two digits are the double
	result.hasDouble || result.currentStreak == 2
}

def hasIncreasingDigits(i: Int): Boolean = toDigits(i).foldLeft((true, -1))((acc, digit) => ((acc._1 && acc._2 <= digit), digit))._1

val goodNumbers =
	for {
		i <- from until to
		if hasDoubleDigitNoTriplet(i)
		if hasIncreasingDigits(i)
	} yield toDigits(i)

println(goodNumbers.map(_.mkString("").toInt))
println(goodNumbers.size)

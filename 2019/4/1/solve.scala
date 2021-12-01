val from = 171309
val to = 643603

def toDigits(i: Int): Seq[Int] = i.toString.map(_.toString.toInt)

def hasDoubleDigit(i: Int): Boolean = toDigits(i).foldLeft((false, -1))((acc, digit) => ((acc._1 || acc._2 == digit), digit))._1

def hasIncreasingDigits(i: Int): Boolean = toDigits(i).foldLeft((true, -1))((acc, digit) => ((acc._1 && acc._2 <= digit), digit))._1

val goodNumbers =
	for {
		i <- from until to
		if hasDoubleDigit(i)
		if hasIncreasingDigits(i)
	} yield toDigits(i)

println(goodNumbers.map(_.mkString("").toInt).take(20))
println(goodNumbers.size)

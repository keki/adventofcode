f = open("input", "r")
input = map(lambda i: int(i), f.readlines())

triplets = zip(input, input[1:], input[2:])

prev = 0
count = 0

for (a, b, c) in triplets:
	sum = a + b + c
	if (prev and sum > prev):
		count += 1
	prev = sum

print count

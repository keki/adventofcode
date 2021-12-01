f = open("input", "r")
input = map(lambda i: int(i), f.readlines())
count = 0
prev = 0
for i in input:
	if (prev and i > prev):
		count += 1
	prev = i

print(count)

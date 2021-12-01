f = open("input", "r")
input = map(lambda i: int(i), f.readlines())


count = 0

prev1 = input.pop(0)
prev2 = input.pop(0)
prevSum = prev1 + prev2 + input[0]
for i in input:
	sum = prev1 + prev2 + i
	if (sum > prevSum):
		count += 1
		print("!")
	else:
		print(".")
	prev1 = prev2
	prev2 = i
	prevSum = sum

print(count)

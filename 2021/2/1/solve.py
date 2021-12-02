f = open("input", "r")

def parseRow(t):
	(direction, valueString) = t.split()
	return (direction, int(valueString))

input = map(parseRow, f.readlines())

horizontalPosition = 0
depth = 0

for (d, v) in input:
	if (d == 'forward'):
		horizontalPosition += v
	elif (d == 'up'):
		depth -= v
	elif (d == 'down'):
		depth += v

#print(horizontalPosition)
#print(depth)
print(horizontalPosition * depth)

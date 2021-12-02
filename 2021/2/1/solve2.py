import numpy as np

def readDirection(d):
	if (d == b'forward'):
		return 1
	elif (d == b'up'):
		return 0 - 1j
	elif (d == b'down'):
		return 0 + 1j

def readAmount(i):
	return complex(int(i),0)

input = np.loadtxt('input', dtype=object, converters = {0: readDirection, 1: readAmount})

#multiply direction and amount for each step
prod = np.prod(input, 1)

#sum steps
sum = np.sum(prod)

print(int(sum.real * sum.imag))

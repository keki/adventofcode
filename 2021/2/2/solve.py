import numpy as np
from functools import partial

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

aim = 0

def take_step(row):
	global aim
	step = row[0] * row[1]
	aim += step.imag
	return complex(step.real, step.real * aim)

sum = np.sum(np.apply_along_axis(take_step, 1, input))

print(int(sum.real * sum.imag))

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

input = np.loadtxt('input', dtype=object, converters = {0: readDirection, 1: readAmount}).prod(axis=1, keepdims=True)

aim = 0

def take_step(row):
	global aim
	step = row[0]
	#step.imag will be zero for forward movements, non-zero for up/down
	aim += step.imag
	# move based on real part and aim
	# won't move if real part is zero (up/down command)
	movement = complex(step.real, step.real * aim)
	return movement

sum = np.sum(np.apply_along_axis(take_step, 1, input))

print(int(sum.real * sum.imag))

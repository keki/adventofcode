import numpy as np

def dirConv(d):
	if (d == b'forward'):
		return 1
	elif (d == b'up'):
		return 0 - 1j
	elif (d == b'down'):
		return 0 + 1j

input = np.loadtxt('input', dtype=object, converters = {0: dirConv, 1: int })

asComplex = np.apply_along_axis(lambda a: a[0] * complex(a[1],0), 1, input)

sum = np.sum(asComplex)

print(int(sum.real * sum.imag))

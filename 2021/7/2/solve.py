import math
import numpy as np

input = np.loadtxt('input', dtype=int, delimiter=',')

mind = np.min(input)
maxd = np.max(input)

def f(d):
	return (d * (d + 1)) / 2

#nem birom ki bocsanat, a python az uj perl
print(int(min([sum(f(abs(input-p))) for p in range(mind,maxd+1)])))

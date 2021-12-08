import math
import numpy as np

input = np.loadtxt('input', dtype=int, delimiter=',')

min_dist = np.min(input)
max_dist = np.max(input)
totals = np.zeros(max_dist+1, dtype = int)

for align_position in range(min_dist, max_dist + 1):
	total_fuel[align_position] = sum(abs(input - align_position))

print("smallest fuel need: ", np.min(totals))

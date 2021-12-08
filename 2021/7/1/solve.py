import math
import numpy as np

positions = np.loadtxt('testinput', dtype=int, delimiter=',')

min_dist = np.min(positions)
max_dist = np.max(positions)
totals = np.zeros(max_dist+1, dtype = int)

for align_position in range(min_dist, max_dist + 1):
	distances = abs(positions - align_position)
	totals[align_position] = sum(distances)

print("smallest fuel need: ", np.min(totals))

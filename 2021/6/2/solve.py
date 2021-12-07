import math
import numpy as np

input = np.loadtxt('input', dtype=int, delimiter=',')

max_timer = 8
days = 256

# count unique values in input
timers = np.zeros(max_timer+1, dtype = int)
for i in input:
	timers[i] += 1

# every day shift the array left and move times[0] to times[8], add previous [0] to [6]
for day in range(1, days+1):
	timers = np.roll(timers, -1)
	timers[6] += timers[8]

print(np.sum(timers))

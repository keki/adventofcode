import math
import numpy as np

input = np.loadtxt('input', dtype=int, delimiter=',')

max_timer = 8
timers = np.zeros(max_timer+1, dtype = int)
days = 80

for i in input:
	timers[i] += 1

#print(input)
#print("start:", timers)
# every day shift one left, 0 goes to 8 and is added to 6
for day in range(1, days+1):
	zeros = timers[0]
	timers = np.roll(timers, -1)
	timers[6] += zeros
	#print(day , ':' , timers)

print(np.sum(timers))

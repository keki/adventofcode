from os import system
from time import sleep
import numpy as np

def read_input():
    input_file = open("input", "r")
    data = []
    row = input_file.readline().strip()

    while row:
        row_split = list(map(int,str(row)))
        data.append(row_split)
        row = input_file.readline().strip()
    return np.array(data)


def flash(dumbos, zeromask):
	flashed = False
	for x in range(1, dumbos.shape[0]-1):
		for y in range(1, dumbos.shape[1]-1):
			if (dumbos[x,y] > 9):
				flashed = True
				dumbos[x-1:x+2,y-1:y+2] += 1
				dumbos[x,y] = 0
				zeromask[x,y] = 0
	return flashed

data = read_input()

# add frame of zeroes around input data
dumbos = np.pad(data, pad_width=1, mode='constant', constant_values=0)

tick_counter = 0
synced = False

while(not synced):
	# create 0/1 mask for frame and future flashed positions
	zeromask = np.pad(np.ones(data.shape, dtype=int), pad_width=1, mode='constant', constant_values=0)

	# increase energy by one, don't worry about frame yet,
	tick_counter +=1
	print("TICK #", tick_counter)
	dumbos += 1

	# clear frame, those should always be zero after each step
	# this is unnecessary as frame will never get to 9 but let's keep it clean
	dumbos *= zeromask

	#start flashing, maintain counter and mask of zeroes for flashed items
	while(flash(dumbos, zeromask)):
		pass

	# clear frame and flashed positions
	dumbos *= zeromask

	synced = (np.sum(dumbos) == 0)

	# show state

	system('clear')
	print("TICK #", tick_counter)
	print(dumbos[1:11,1:11])
	sleep(0.2)

print("TICKS: ", tick_counter)

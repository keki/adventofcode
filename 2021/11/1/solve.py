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


def flash(dumbos, flash_counter, zeromask):
	flashed = False
	for x in range(1, dumbos.shape[0]-1):
		for y in range(1, dumbos.shape[1]-1):
			if (dumbos[x,y] > 9):
				flash_counter += 1
				flashed = True
				dumbos[x-1:x+2,y-1:y+2] += 1
				dumbos[x,y] = 0
				zeroframe[x,y] = 0
	return (flashed, flash_counter, zeromask)

data = read_input()

# add frame of zeroes around input data
dumbos = np.pad(data, pad_width=1, mode='constant', constant_values=0)

flash_counter = 0
for i in range(0,100):
	# create 0/1 mask for frame and future flashed positions
	zeroframe = np.pad(np.ones(data.shape, dtype=int), pad_width=1, mode='constant', constant_values=0)

	# increase energy by one, don't worry about frame yet,
	print("TICK #", i)
	dumbos += 1
	# clear frame, those should always be zero after each step
	# this is unnecessary as frame will never get to 9 but let's keep it clean
	dumbos *= zeroframe

	#start flashing, maintain counter and mask of zeroes for flashed items
	(flashed, flash_counter, zeromask) = flash(dumbos, flash_counter, zeroframe)
	while(flashed):
		(flashed, flash_counter, zeromask) = flash(dumbos, flash_counter, zeromask)

	# clear frame and flashed positions
	dumbos *= zeromask

	# show state
	print(dumbos[1:11,1:11])

print("Number of flashes: ", flash_counter)

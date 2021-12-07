import math
import numpy as np

#read stuff from file
def to_coords(s):
	(x, y) = map(int, s.decode('UTF-8').split(","))
	return np.array([x, y])

vectors = np.loadtxt('input', dtype=object, delimiter=' -> ', converters={0: to_coords, 1: to_coords})

#
# initialize board
#

max_x = vectors[:,:,1].max()
max_y = vectors[:,:,0].max()
board = np.zeros((max_x+1, max_y+1), dtype=int)


# pick start and end of vectors (start has lower coordinate)
def start_end(v1, v2, coord):
	if (v1[coord] < v2[coord]):
		return (v1, v2)
	else:
		return (v2, v1)

# draw a vector
def draw_vector(vector):
	start = vector[0]
	end = vector[1]

	# """"named"""" columns! :)
	# x and y coordinate order is flipped to get a nice print(board) output
	x = 1
	y = 0
	x_delta = end[x] - start[x]
	y_delta = end[y] - start[y]
	x_dir = np.sign(x_delta)
	y_dir = np.sign(y_delta)

	# create x and y coordinate ranges (a real range or just fill with zeros)
	if(x_delta != 0):
		x_range = np.array(range(0, x_delta + x_dir, x_dir), dtype=int)
	else:
		x_range = np.zeros(abs(y_delta)+1, dtype=int)
	if(y_delta != 0):
		y_range = np.array(range(0, y_delta + y_dir, y_dir), dtype=int)
	else:
		y_range = np.zeros(abs(x_delta)+1, dtype=int)

	# np.c_ zips two arrays
	vector_points = np.c_[x_range, y_range]

	# now we just draw the calculated points on the board
	for (x_step,y_step) in vector_points:
		board[start[x] + x_step, start[y] + y_step] += 1


#
# draw all vectors on board
#
for i in range(0, vectors.shape[0]):
	draw_vector(vectors[i])

print(board)

#
# get count of different danger levels
#
(danger_levels, danger_counts) = np.unique(board, return_counts=True)

for i in range(1, danger_levels.size):
	print("danger count at level ", danger_levels[i],": ", danger_counts[i])

print("number of lvl2+ dangerous places:", sum(danger_counts[2:]))

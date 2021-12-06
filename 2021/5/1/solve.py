import math
import numpy as np

#read stuff from file
def to_coords(s):
	(x, y) = map(int, s.decode('UTF-8').split(","))
	#return {"x": x, "y": y}
	return np.array([x, y])

input = np.loadtxt('input', dtype=object, delimiter=' -> ', converters={0: to_coords, 1: to_coords})

#
# filter input for horizontal and vertical vectors
#

input_size = input.shape[0]

def is_horizontal(v):
	return v[0,1] == v[1,1]

def is_vertical(v):
	return v[0,0] == v[1,0]

vectors = np.array([input[i] for i in range(0, input_size) if (is_horizontal(input[i]) or is_vertical(input[i]))])

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
# x and y coordinates are flipped to get a nice print(board) output
def draw_vector(vector):
	if (vector[0][0] == vector[1][0]):
		(start, end) = start_end(vector[0], vector[1], 1)
		x = start[0]
		for y in range(start[1], end[1]+1):
			board[y,x] += 1
	else:
		(start, end) = start_end(vector[0], vector[1], 0)
		y = start[1]
		for x in range(start[0], end[0]+1):
			board[y,x] +=1
#
# draw all vectors on board
#
for i in range(0, vectors.shape[0]):
	draw_vector(vectors[i])

#
# count different danger levels
#
(danger_levels, danger_counts) = np.unique(board, return_counts=True)

for i in range(1, danger_levels.size):
	print("danger count at level ", danger_levels[i],": ", danger_counts[i])

print("number of lvl2+ dangerous places:", sum(danger_counts[2:]))

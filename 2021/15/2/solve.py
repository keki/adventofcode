import numpy as np
from os import system

def read_input():
    input_file = open("input", "r")
    data = []
    row = input_file.readline().strip()

    while row:
        row_split = list(map(int,str(row)))
        data.append(row_split)
        row = input_file.readline().strip()
    return np.array(data)

def generate_full_map(cave_map):
    width = cave_map.shape[0]
    height = cave_map.shape[1]
    full_map = np.zeros((width*5, height*5), dtype=int)
    for i in range(0,5):
        for j in range(0,5):
            x = i*width
            y = j*height
            new_map = cave_map + (i + j)
            new_map = np.where(new_map > 9, new_map - 9, new_map)
            full_map[x:x+width,y:y+height] = new_map
    return full_map

def set_distance(point, distance):
    global distance_map
    global mapped_points
    x = point[0]
    y = point[1]
    distance_map[x, y] = distance
    mapped_points.add((x,y))

def neighbors_of(point):
    x = point[0]
    y = point[1]
    return set([(x+i,y+j) for (i,j) in [(-1,0),(1,0),(0,1),(0,-1)] if cave_map[x+i,y+j] != -2])

def all_neighbors_of(points):
    res = set()
    for point in points:
        res.add(neighbors_of(point))
    return res

def is_mapped(point):
    return distance_map[point] != -1

def shortest_path_to(point):
    neighbor_distances = [distance_map[n] for n in neighbors_of(point) if is_mapped(n)]
    min_neighbor_distance = np.amin(neighbor_distances)
    return min_neighbor_distance + cave_map[point]

cave_map = generate_full_map(read_input())
distance_map = np.full(cave_map.shape, -1, dtype=int)
cave_map = np.pad(cave_map, pad_width=1, mode='constant', constant_values=-2)
distance_map = np.pad(distance_map, pad_width=1, mode='constant', constant_values=-2)
mapped_points = set()
set_distance((1,1),0)
map_next = neighbors_of((1,1))

while (map_next):
    new_map_next = set()
    for point in map_next:
        # get shortest path from already mapped neighbors
        dist = shortest_path_to(point)
        if (not is_mapped(point) or dist < distance_map[point]):
            # set new distance if not mapped yet or found a better path
            set_distance(point, dist)
            for n in neighbors_of(point):
                # add neighbors to the "to be mapped next" set
                # only if not mapped yet or there is a chance for improvement
                if (not is_mapped(n) or distance_map[n] > dist + cave_map[n]):
                    new_map_next.add(n)
    system('clear')
    print("UNMAPPED:", np.count_nonzero(distance_map == -1))
    print("MAPNEXT:", len(new_map_next))
    map_next = new_map_next

print(distance_map)

import numpy as np

def read_heightmap():
    input_file = open("input", "r")
    heightmap = []
    row = input_file.readline().strip()
    while row:
        row_split = list(map(int, str(row)))
        heightmap.append(row_split)
        row = input_file.readline().strip()
    return(np.array(heightmap))

def init_basinmap(heightmap):
    map_width = heightmap.shape[0]
    map_height = heightmap.shape[1]
    basinmap = np.zeros((map_width, map_height), dtype=int)
    basin_id = 1

    def is_low_point(i,j):
        n = (i == 0 or heightmap[i,j] < heightmap[i-1,j])
        s = (i == map_height - 1 or heightmap[i,j] < heightmap[i+1,j])
        w = (j == 0 or heightmap[i,j] < heightmap[i,j-1])
        e = (j == map_width - 1 or heightmap[i,j] < heightmap[i,j+1])
        return (n and e and w and s)

    for i in range(0, map_width):
        for j in range(0, map_height):
            if (is_low_point(i,j)):
                basinmap[i,j] = basin_id
                basin_id += 1

    return basinmap

def grow_basinmap(basinmap, heightmap):
    map_width = heightmap.shape[0]
    map_height = heightmap.shape[1]
    found_new_basin_position = False

    def find_basin_neighbor(i,j):
        if (i != 0 and basinmap[i-1,j] != 0):
            return basinmap[i-1,j]
        elif (i != map_height - 1 and basinmap[i+1,j] != 0):
            return basinmap[i+1,j]
        elif (j != 0 and basinmap[i,j-1] != 0):
            return basinmap[i,j-1]
        elif (j != map_width - 1 and basinmap[i,j+1] != 0):
            return basinmap[i,j+1]
        else:
            return 0

    for i in range(0, map_width):
        for j in range(0, map_height):
            if (heightmap[i,j] != 9 and basinmap[i,j] == 0):
                # not a 9 height and we haven't mapped it either
                neighboring_basin = find_basin_neighbor(i,j)
                if (neighboring_basin):
                    basinmap[i,j] = neighboring_basin
                    found_new_basin_position = True

    return found_new_basin_position

heightmap = read_heightmap()
basinmap = init_basinmap(heightmap)

print("HEIGHTS:\n", heightmap[:20,:20])
print("BASINS:\n", basinmap[:20, :20])

while(grow_basinmap(basinmap, heightmap)):
    print("growing basins...")

print("BASINS:\n", basinmap[:20, :20])

basin_sizes = np.unique(basinmap, return_counts=True)[1][1:]
sorted_basin_sizes = sorted(basin_sizes, reverse=True)[:3]

print("LARGEST BASINS:", sorted_basin_sizes)

print("SOLUTION: ", np.prod(sorted_basin_sizes))


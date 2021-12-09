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

def risk_levels(heightmap):
    map_width = heightmap.shape[0]
    map_height = heightmap.shape[1]
    riskmap = np.zeros((map_width, map_height), dtype=int)

    def is_low_point(i,j):
        n = (i == 0 or heightmap[i,j] < heightmap[i-1,j])
        e = (i == map_height - 1 or heightmap[i,j] < heightmap[i+1,j])
        w = (j == 0 or heightmap[i,j] < heightmap[i,j-1])
        s = (j == map_width - 1 or heightmap[i,j] < heightmap[i,j+1])
        return (n and e and w and s)

    for i in range(0, map_width):
        for j in range(0, map_height):
            if( is_low_point(i,j)):
                riskmap[i,j] = heightmap[i,j] + 1
    return riskmap

heightmap = read_heightmap()
riskmap = risk_levels(heightmap)

print("HEIGHTS:\n", heightmap[:20,:20])
print("RISK LEVELS:\n", riskmap[:20, :20])
print("LOW POINT COUNT: ", np.sum(riskmap))

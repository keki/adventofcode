import numpy as np
from os import system
from itertools import permutations

#
# OK THIS WAS A STRUGGLE
#

def read_input():
    input_file = open("input", "r")
    data = []
    scanner = []
    row = input_file.readline().strip()
    while row:
        if(row[0] == '-'):
            if (scanner):
                data.append(np.array(scanner))
            scanner = []
            row = input_file.readline().strip()
        while row:
            coords = list(map(int,row.split(',')))
            scanner.append(np.array(coords))
            row = input_file.readline().strip()
        row = input_file.readline().strip()
    data.append(np.array(scanner))
    return data

def to_distances(scanner_data):
    distances = []
    for i, v1 in enumerate(scanner_data):
        for j, v2 in enumerate(scanner_data):
            if (i > j):
                distance = np.sum((v1 - v2) ** 2)
                distances.append(distance)
    return np.array(distances)

def count_same_distances(dd1, dd2):
    done = False
    matches = 0
    for i, d1 in enumerate(dd1):
        for j, d2 in enumerate(dd2):
            if (d1 == d2):
                matches += 1
    return matches

# normalize scanner data to a given point in it (make that point 0,0,0)
def normalizations(sd):
    return [sd - d for d in sd]

def rotations(sd):
    rotas = []
    for axis in permutations([0,1,2]):
        for x_dir in 1, -1:
            for y_dir in 1, -1:
                for z_dir in 1, -1:
                    rotated = []
                    for v in sd:
                        rotated.append([v[axis[0]] * x_dir, v[axis[1]] * y_dir, v[axis[2]] * z_dir])
                    rotas.append(rotated)
    return np.array(rotas)

def matches(sd1, sd2):
    m = 0
    for v1 in sd1:
        for v2 in sd2:
            if (np.array_equal(v1, v2)):
                m += 1
    return m

data = read_input()

print("GENERATE DISTANCE MAPS")
distance_data = [to_distances(sd) for sd in data]

# (12 * 11) / 2 = 66 distances have to match if at least 12 points are the same
possible_matches = {}
print("CHECKING DISTANCES")
for i, dd1 in enumerate(distance_data):
    for j, dd2 in enumerate(distance_data):
        if (i < j):
            same_dist_count = count_same_distances(dd1, dd2)
            if (same_dist_count >= 66):
                print("POSSIBLE MATCH:", i, j, same_dist_count)
                if(i in possible_matches):
                    possible_matches[i].append(j)
                else:
                    possible_matches[i] = [j]

print(possible_matches)

print("GENERATE SCANNER DATA VERSIONS")
beacon_count = 0
full_data = []
for i, sd in enumerate(data):
    beacon_count += len(sd)
    full_data.append(rotations(sd))

def distances_from(point, scanner_data):
    distances = []
    for v in scanner_data:
        distance = np.sum((point - v) ** 2)
        distances.append(distance)
    return distances

def matching_distances(ds1, ds2):
    matches = []
    for i, d1 in enumerate(ds1):
        for j, d2 in enumerate(ds2):
            if(d1 == d2):
                matches.append([i, j])
    return matches

def matching_transform(scanner_data, rotations):
    for r in rotations:
        for v1 in scanner_data:
            for v2 in r:
                possible_transform = v2 - v1
                dist_matches = matching_distances(distances_from(v1, scanner_data), distances_from(v2, r))
                match_count = 0
                for (i, j) in dist_matches:
                    if (np.array_equal(scanner_data[i], r[j] - possible_transform)):
                        match_count +=1
                        if (match_count >= 12):
                            break
                if (match_count >= 12):
                    transform = possible_transform
                    rt = r - transform
                    return (rt, transform)

matched = {}
matched[0] = data[0]
transforms = []
found = True
while (found):
    found = False
    print(matched.keys())
    for i in possible_matches:
        for j in possible_matches[i]:
            print(i,j)
            if (i in matched):
                if (j in matched):
                    pass
                else:
                    (transformed, transform) = matching_transform(matched[i], full_data[j])
                    found = True
                    matched[j] = transformed
                    transforms.append((i, j, transform))
            else:
                if (j in matched):
                    (transformed, transform) = matching_transform(matched[j], full_data[i])
                    found = True
                    matched[i] = transformed
                    transforms.append((j, i, transform))
                else:
                    pass

    if (i in matched):
        pass
    else:
        for j in possible_matches[i]:

            if (not transformed is None):
                matched[j] = transformed
                possible_matches[i].remove(j)

print(matched)


beacons = set()
for k in matched:
    for b in matched[k]:
        beacons.add((b[0],b[1],b[2]))

print("BEACON COUNT:", len(beacons))

print("TRANSFORMS:", transforms)

transforms_from_zero = np.full((len(data), 3), [0,0,0])
for t in transforms:
    transforms_from_zero[t[1]] = t[2]

max_manhattan = 0

for t1 in transforms_from_zero:
    for t2 in transforms_from_zero:
        print(abs(t1-t2))
        manhattan = sum(abs(t1 - t2))
        if(max_manhattan < manhattan):
            max_manhattan = manhattan

print("MAX MANHATTAN:", max_manhattan)

print(transforms_from_zero)

import numpy as np

input_file = open("input", "r")
rules = {}

polymer = list(map(lambda i: i, input_file.readline().strip()))

input_file.readline().strip() # empty row

row = input_file.readline().strip()
while row:
    row_split = list(map(lambda s: s.strip(), row.split('->')))
    rules[row_split[0]] = row_split[1]
    row = input_file.readline().strip()

def cut_to_chunks(poly):
    return [''.join([poly[p], poly[p+1]]) for p in range(0, len(poly)-1)]

def add_to_arr(arr, key, n):
    if (key in arr):
        arr[key] += n
    else:
        arr[key] = n

# initialize chunk stats
chunk_stats = {}
for chunk in cut_to_chunks(polymer):
    add_to_arr(chunk_stats, chunk, 1)

# ok, brute force doesn't work this time, go batched
for round in range(0,40):
    new_chunk_stats = {}
    for chunk in chunk_stats:
        count = chunk_stats[chunk]
        new_char = rules[chunk]
        if (new_char):
            chunk_left = ''.join([chunk[0], new_char])
            chunk_right = ''.join([new_char, chunk[1]])
            add_to_arr(new_chunk_stats, chunk_left, count)
            add_to_arr(new_chunk_stats, chunk_right, count)
    chunk_stats = new_chunk_stats

print(chunk_stats)

# char stats from chunk stats
char_stats = {}
for chunk in chunk_stats:
    add_to_arr(char_stats, chunk[0], chunk_stats[chunk])
    add_to_arr(char_stats, chunk[1], chunk_stats[chunk])

# first and last char is only counted once, while everything else is counted twice
add_to_arr(char_stats, polymer[0], 1)
add_to_arr(char_stats, polymer[-1], 1)

minvalue = 0
maxvalue = 0
for char in char_stats:
    value = int(char_stats[char] / 2)
    if (minvalue == 0 or value < minvalue):
        minvalue = value
    if (maxvalue == 0 or value > maxvalue):
        maxvalue = value

print("MAX:", maxvalue)
print("MIN:", minvalue)
print("RESULT: ", maxvalue - minvalue)


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

for round in range(0, 10):
    new_polymer = []
    for p in range(0, len(polymer)-1):
        new_polymer.append(polymer[p])
        chunk = ''.join([polymer[p],polymer[p+1]])
        if (chunk in rules):
            new_polymer.append(rules[chunk])
    new_polymer.append(polymer[-1])
    polymer = new_polymer

# super convoluted "numpythonic" way to count max & min
polymer = np.array(polymer)
(unique_elements, counts) = np.unique(polymer, return_counts = True)
counts_sort_ind = np.argsort(-counts)
print(counts[counts_sort_ind])
print(unique_elements[counts_sort_ind])
print("RESULT: ", counts[counts_sort_ind][0] - counts[counts_sort_ind][-1])


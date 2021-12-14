import numpy as np

input_file = open("input", "r")
rules = []

polymer = list(map(lambda i: i, input_file.readline().strip()))

input_file.readline().strip() # empty row

row = input_file.readline().strip()
while row:
    row_split = list(map(lambda s: s.strip(), row.split('->')))
    row_split[0] = list(map(lambda c: c, row_split[0]))
    rules.append(row_split)
    row = input_file.readline().strip()

print(polymer)
print(rules)

def is_a_match(polymer, p, rule):
    return rule[0][0] == polymer[p] and rule[0][1] == polymer[p+1]

for round in range(0, 10):
    print("ROUND #",round+1)
    new_polymer = []
    for p in range(0, len(polymer)-1):
        new_polymer.append(polymer[p])
        for rule in rules:
            if (is_a_match(polymer, p, rule)):
                new_polymer.append(rule[1])
    new_polymer.append(polymer[-1])
    polymer = new_polymer
    print(''.join(polymer))

polymer = np.array(polymer)

(unique_elements, counts) = np.unique(polymer, return_counts = True)
counts_sort_ind = np.argsort(-counts)
print(counts[counts_sort_ind])
print(unique_elements[counts_sort_ind])
print("RESULT: ", counts[counts_sort_ind][0] - counts[counts_sort_ind][-1])


import numpy as np

data = np.loadtxt('input', dtype=str)

unique_code_lengths = set([2,3,4,7])
outputs = data[:,11:]

def code_lengths(arr):
 return [len(code) in unique_code_lengths for code in arr]

codes_with_unique_lengths = np.apply_along_axis(code_lengths, 1, outputs)

print(np.count_nonzero(codes_with_unique_lengths))

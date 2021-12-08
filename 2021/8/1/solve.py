import numpy as np

data = np.loadtxt('input', dtype=str)

unique_lengths = set([2,3,4,7])
outputs = data[:,11:]

def code_lengths(a):
 return [len(i) in unique_lengths for i in a]

codes_with_unique_lengths = np.apply_along_axis(code_lengths, 1, outputs)

print(np.count_nonzero(codes_with_unique_lengths))

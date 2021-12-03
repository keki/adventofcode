import numpy as np

# convert string to array of digits
def split_str(s):
  return [int(ch) for ch in s]

# convert [1, 0, 0, 1] to 9
def bin_arr_to_int(a):
	return int(''.join(map(str, a)),2)

# there must be a nicer way to do this
input = np.loadtxt('input', dtype=str)
digits = np.array(list(map(split_str, input)))

entries = digits.shape[0]

# count ones and zeroes
gamma_arr = np.median(digits, 0).astype(int)
epsilon_arr = np.vectorize(lambda x: 1 - x)(gamma_arr)

gamma = bin_arr_to_int(gamma_arr)
epsilon = bin_arr_to_int(epsilon_arr)

print(gamma * epsilon)

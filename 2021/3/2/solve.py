import math
import numpy as np

# convert string to array of digits
def split_str(s):
  return [int(ch) for ch in s]

# convert [1, 0, 0, 1] to 9
def bin_arr_to_int(a):
	return int(''.join(map(str, a)),2)

# there must be a nicer way to do this, but this gets input into an array of array of digits
input = np.loadtxt('input', dtype=str)
digits = np.array(list(map(split_str, input)))

def most_common_bit(arr, pos):
	# round(0.5) == 0 in python, but round(1.5) == 2. WTF. SAD.
	return math.floor(np.median(arr[:,pos]) + 0.5)

def least_common_bit(arr, pos):
	return 1 - most_common_bit(arr, pos)

def get_rating(arr, f):
	result = arr.copy()
	pos = 0
	# no tail recursion optimization in python. SAD.
	while (result.shape[0] > 1):
		bit_value_at_pos = f(result, pos)
		# arr.filter(a => a(pos) == value) but in a pythonic way. SAD.
		result = np.array([a for a in result if a[pos] == bit_value_at_pos])
		pos += 1
	return bin_arr_to_int(result[0])

oxygen_generator_rating = get_rating(digits, most_common_bit)
co2_generator_rating = get_rating(digits, least_common_bit)

print(oxygen_generator_rating * co2_generator_rating)

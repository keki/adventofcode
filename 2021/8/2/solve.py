import numpy as np
import itertools

data = np.loadtxt('input', dtype=str)

digits_as_segments = [
	[True, True, True, False,True, True, True ], #0
	[False,False,True, False,False,True, False], #1
	[True, False,True, True, True, False,True ], #2
	[True, False,True, True, False,True, True ], #3
	[False,True, True, True, False,True, False], #4
	[True, True, False,True, False,True, True ], #5
	[True, True, False,True, True, True, True ], #6
	[True, False,True, False,False,True, False], #7
	[True, True, True, True, True, True, True ], #8
	[True, True, True, True, False,True, True ]  #9
]

letters = ['a','b','c','d','e','f','g']
all_encodings = list(itertools.permutations(letters,7))

def as_bool_array(code, encoding):
	decoded_segments = [encoding.index(char) for char in code]
	return [(i in decoded_segments) for i in range(0,len(encoding))]

def is_decodeable(codes, encoding):
	for code in codes:
		if(code != '|'):
			decoded = as_bool_array(code, encoding)
			if (not decoded in digits_as_segments):
				return False
	return True

def find_encoding(codes):
	for encoding in all_encodings:
		if (is_decodeable(codes, encoding)):
			return(encoding)

# this can be only called with valid encodings
def decode(code, encoding):
	digits_as_array = str(digits_as_segments.index(as_bool_array(code, encoding)))
	return digits_as_array

summa = 0

for codes in data:
	encoding = find_encoding(codes)
	outputs = codes[11:]
	decoded_output_as_array = [decode(code, encoding) for code in outputs]
	decoded_output = int("".join(decoded_output_as_array))
	summa += decoded_output
	print("DECODED:  ", decoded_output)

print ("SUM OF OUTPUTS: ", summa)

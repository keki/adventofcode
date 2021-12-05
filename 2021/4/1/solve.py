import numpy as np

import math
import numpy as np

#read stuff from file
numbers = np.loadtxt('input', dtype=int, delimiter=',', max_rows=1)
sheets_tmp = np.loadtxt('input', dtype=int, skiprows=2)
sheet_size = sheets_tmp.shape[1]
num_of_sheets = int(sheets_tmp.shape[0] / sheet_size)
sheets = sheets_tmp.reshape(num_of_sheets, sheet_size, sheet_size)

# check if all elements of arr1 is in arr2
def bingo(arr1, arr2):
	return not(set(arr1) - set(arr2))

def run_bingo():
	for round in range(1, len(numbers)):
		for sheet in range(0, num_of_sheets):
			for row_or_col in range(0, sheet_size):
				if (bingo(sheets[sheet, row_or_col], numbers[:round]) or bingo(sheets[sheet, :, row_or_col], numbers[:round])):
					return (sheets[sheet], numbers[:round])

# winner found, calculate result
(sheet, called_numbers) = run_bingo()

unmarked_on_sheet = set(sheet.flatten()) - set(called_numbers)
unmarked_sum = sum(unmarked_on_sheet)

print("sheet:", sheet)
print("last called number:", called_numbers[-1])
print("unmarked:", unmarked_on_sheet, " - sum:", unmarked_sum)

print("result:", unmarked_sum * called_numbers[-1])


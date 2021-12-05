import numpy as np

import math
import numpy as np

numbers = np.loadtxt('input', dtype=int, delimiter=',', max_rows=1)
sheets_tmp = np.loadtxt('input', dtype=int, skiprows=2)

sheet_size = sheets_tmp.shape[1]
num_of_sheets = int(sheets_tmp.shape[0] / sheet_size)

sheets = sheets_tmp.reshape(num_of_sheets, sheet_size, sheet_size)

# check if all elements of arr1 is in arr2
def bingo(arr1, arr2):
	return not(set(arr1) - set(arr2))

def rounds_to_bingo(sheet):
	# check each sheet
	for round in range(1, len(numbers)):
		for row_or_col in range(0, sheet_size):
			if(bingo(sheets[sheet, row_or_col], numbers[:round]) or bingo(sheets[sheet, :, row_or_col], numbers[:round])):
				return round

# calculate winning round for each sheet
winning_rounds_by_sheet = [rounds_to_bingo(s) for s in range(0, num_of_sheets)]

# pick last-to-win sheet
last_round = max(winning_rounds_by_sheet)
last_sheet_id = winning_rounds_by_sheet.index(last_round)
sheet = sheets[last_sheet_id]

# calculate remaining numbers
called_numbers = numbers[:last_round]
last_call = called_numbers[-1]

unmarked_on_sheet = set(sheet.flatten())-set(called_numbers)
unmarked_sum = sum(unmarked_on_sheet)

print("sheet:", sheet)
print("last:", last_call)
print("unmarked:", unmarked_on_sheet, " - sum:", unmarked_sum)

print("result:", unmarked_sum * last_call)


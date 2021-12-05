import numpy as np

import math
import numpy as np

numbers = np.loadtxt('input', dtype=int, delimiter=',', max_rows=1)
sheets_tmp = np.loadtxt('input', dtype=int, skiprows=2)

sheet_size = sheets_tmp.shape[1]
num_of_sheets = int(sheets_tmp.shape[0] / sheet_size)

sheets = sheets_tmp.reshape(num_of_sheets, sheet_size, sheet_size)

# check if all elements of a given array is in the numbers
def bingo(arr, n):
	return not(set(arr) - set(n))

def find_bingo(sheet):

	# check each sheet
	for i in range(1, len(numbers)):
		called_numbers = numbers[:i]

		# check rows
		for row in range(0, sheet_size):
			r = sheet[row]
			if(bingo(r, called_numbers)):
				print("row:", r)
				return i

		#check columns
		for col in range(0, sheet_size):
			c = sheet[:, col]
			if(bingo(c, called_numbers)):
				print("column:", c)
				return i

		#check diagonals
		d1 = np.diagonal(sheet)
		if(bingo(d1, called_numbers)):
				print("diagonal:", d1)
				return i
		d2 = np.flipud(sheet).diagonal()
		if(bingo(d2, called_numbers)):
				print("diagonal:", d2)
				return i

	# this sheet never wins
	return len(numbers)

def run_bingo():
	sheet_results = [find_bingo(sheets[i]) for i in range(0, num_of_sheets)]
	return sheet_results

# calculate winning round for each sheet
winning_round_by_sheet = run_bingo()

# pick last-to-win sheet
last_round = max(winning_round_by_sheet)
last_sheet_id = winning_round_by_sheet.index(last_round)
sheet = sheets[last_sheet_id]

# calculate remaining numbers
called_nums = numbers[:last_round]
sheet_sum = np.sum(sheet)

unmarked_on_sheet = set(sheet.flatten())-set(called_nums)
unmarked_sum = sum(unmarked_on_sheet)

print("sheet:", sheet, " - sum: ", sheet_sum)
print("last:", called_nums[-1])
print("unmarked:", unmarked_on_sheet, " - sum:", unmarked_sum)
print("result:", unmarked_sum * called_nums[-1])


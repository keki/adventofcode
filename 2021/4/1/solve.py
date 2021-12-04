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

def find_bingo(round):
	called_numbers = numbers[:round]

	# check each sheet
	for s in range(0, num_of_sheets):
		sheet = sheets[s]

		# check rows
		for row in range(0, sheet_size):
			r = sheet[row]
			if(bingo(r, called_numbers)):
				print("row:", r)
				return (sheet, r, called_numbers)

		#check columns
		for col in range(0, sheet_size):
			c = sheet[:, col]
			if(bingo(c, called_numbers)):
				print("column:", c)
				return (sheet, c, called_numbers)

		#check diagonals
		d1 = np.diagonal(sheet)
		if(bingo(d1, called_numbers)):
				print("diagonal:", d1)
				return (sheet, d1, called_numbers)
		d2 = np.flipud(sheet).diagonal()
		if(bingo(d2, called_numbers)):
				print("diagonal:", d2)
				return (sheet, d2, called_numbers)

	# no winner this round
	return (None, None, None)

def run_bingo(nums):
	# no need to check bingo before seet_size numbers called
	for i in range(sheet_size, len(nums)):
		(sheet, bingo, called_nums) = find_bingo(i)
		if (not (bingo is None)):
			return (sheet, bingo, called_nums)

(sheet, bingo, called_nums) = run_bingo(numbers)
sheet_sum = np.sum(sheet)
unmarked_on_sheet = set(sheet.flatten())-set(called_nums)
unmarked_sum = sum(unmarked_on_sheet)

print("sheet:", sheet, " - sum: ", sheet_sum)
print("last:", called_nums[-1])
print("unmarked:", unmarked_on_sheet, " - sum:", unmarked_sum)

print("result:", unmarked_sum * called_nums[-1])

#print("result:", (sheet_sum - bingo_sum) * last_num)


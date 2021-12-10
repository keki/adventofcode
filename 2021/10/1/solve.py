import numpy as np

def read_input():
    input_file = open("input", "r")
    brackets = []
    row = input_file.readline().strip()
    while row:
        row_split = list(map(str,str(row)))
        brackets.append(row_split)
        row = input_file.readline().strip()
    return brackets

brackets = read_input()

open_brackets = ['(','[','<','{']
close_brackets = [')',']','>','}']
bracket_scores = { ')': 3, ']': 57, '}': 1197, '>': 25137}
corruption_score = 0

for row in brackets:
    bracket_stack = []
    for char in row:
        if (char in open_brackets):
            bracket_stack.append(char)
        else:
            close_bracket_type = close_brackets.index(char)
            open_bracket_type = open_brackets.index(bracket_stack[-1])
            if (open_bracket_type == close_bracket_type):
                bracket_stack.pop()
            else:
                corruption_score += bracket_scores[char]
                break

print(corruption_score)


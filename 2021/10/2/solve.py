import numpy as np

open_brackets = ['(','[','<','{']
close_brackets = [')',']','>','}']
bracket_scores = { ')': 1, ']': 2, '}': 3, '>': 4}

def read_input():
    input_file = open("input", "r")
    brackets = []
    row = input_file.readline().strip()
    while row:
        row_split = list(map(str,str(row)))
        brackets.append(row_split)
        row = input_file.readline().strip()
    return brackets


def flip_bracket(char):
    return close_brackets[open_brackets.index(char)]

def reverse_bracket_stack(bracket_stack):
    reversed_bracket_stack = bracket_stack[::-1]
    flipped_bracket_stack = list(map(flip_bracket, reversed_bracket_stack))
    return flipped_bracket_stack

def calculate_missing_bracket_score(brackets):
    score = 0
    for bracket in brackets:
        bracket_value = bracket_scores[bracket]
        score = score * 5 + bracket_value
    return score

def middle_score(scores):
    # sort mutates the input array ZOMG
    scores.sort()
    return scores[int(len(scores) / 2)]

brackets = read_input()

row_scores = []
for row in brackets:
    bracket_stack = []
    missing_brackets = []
    for char in row:
        if (char in open_brackets):
            bracket_stack.append(char)
        else:
            close_bracket_type = close_brackets.index(char)
            open_bracket_type = open_brackets.index(bracket_stack[-1])
            if (open_bracket_type == close_bracket_type):
                bracket_stack.pop()
            else:
                bracket_stack = []
                break
    if (bracket_stack):
        missing_brackets = reverse_bracket_stack(bracket_stack)
        row_scores.append(calculate_missing_bracket_score(missing_brackets))


print(middle_score(row_scores))


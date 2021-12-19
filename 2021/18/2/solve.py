from itertools import combinations

def read_input():
    input_file = open("input", "r")
    data = []
    row = input_file.readline().strip()
    while row:
        row_split = list(map(lambda c:c,str(row)))
        data.append(as_array(row_split))
        row = input_file.readline().strip()
    return data

def as_array(row):
    arr = []
    for char in row:
        if (char == '[' or char == ']' or char == ','):
            arr.append(char)
        else:
            if (isinstance(arr[-1], int)):
                # already read the first digits of this number
                arr[-1] = arr[-1] * 10 + int(char)
            else:
                arr.append(int(char))
    return arr

def as_obj(arr):
    number = {}
    elem = arr.pop(0)
    if (elem == '['):
        number['left'] = as_obj(arr)
        # consume the comma
        arr.pop(0)
        number['right'] = as_obj(arr)
        # consume the ']'
        arr.pop(0)
    else:
        number['value'] = int(elem)
    return number

def find_explosion_index(arr):
    lvl = 0
    for i, v in enumerate(arr):
        if (v == '['):
            if (lvl == 4):
                return i
            else:
                lvl += 1
        elif (v == ']'):
            lvl -= 1

def find_last_numeric_before(arr, index):
    for i in range(index, 0, -1):
        if (isinstance(arr[i],int)):
            return i

def find_first_numeric_after(arr, index):
    for i in range(index, len(arr)):
        if (isinstance(arr[i],int)):
            return i

def find_close_bracket(arr, open_bracket_index):
    # items to explode are always just two plain numbers, the first close bracket will be fine
    for i in range(open_bracket_index, len(arr)):
        if (arr[i] == ']'):
              return i

def explode_at(arr, index):
    close_bracket_index = find_close_bracket(arr, index)

    left_value = arr[index + 1]
    right_value = arr[index + 3]

    left_numeric_index = find_last_numeric_before(arr, index)
    if (left_numeric_index):
        arr[left_numeric_index] += left_value

    right_numeric_index = find_first_numeric_after(arr, close_bracket_index)
    if (right_numeric_index):
        arr[right_numeric_index] += right_value

    return arr[:index] + [0] + arr[close_bracket_index+1:]

def as_string(arr):
    s = ""
    for item in arr:
        if (isinstance(item, int)):
            s += str(item)
        else:
            s += item
    return s

def half_round_up(i):
    if (i % 2):
        return int((i+1) / 2)
    else:
        return int(i / 2)

def half_round_down(i):
    if (i % 2):
        return int((i-1) / 2)
    else:
        return int(i / 2)

def find_split_index(arr):
    for i in range(0, len(arr)):
        if(isinstance(arr[i], int)):
            if(arr[i] >= 10):
                return i

def split_at(arr, i):
    new_pair = ['[', half_round_down(arr[i]), ',', half_round_up(arr[i]), ']']
    return arr[:i] + new_pair + arr[i+1:]

def reduce_number(arr):
    changed = True
    while (changed):
        changed = False
        explosion_index = find_explosion_index(arr)
        if (explosion_index):
            changed = True
            arr = explode_at(arr, explosion_index)
        else:
            split_index = find_split_index(arr)
            if (split_index):
                changed = True
                arr = split_at(arr, split_index)
    return arr

def add(arr1, arr2):
    return reduce_number(["["] + arr1 + [","] + arr2 + ["]"])

def magnitude(obj):
    if ('value' in obj):
        return obj['value']
    else:
        return 3 * magnitude(obj['left']) + 2 * magnitude(obj['right'])

data = read_input()
pairs = combinations(data, 2)
max_magnitude = 0
for (a,b) in pairs:
    m = max(magnitude(as_obj(add(a,b))),magnitude(as_obj(add(b,a))))
    if (m > max_magnitude):
        max_magnitude = m

print(f"RESULT: {max_magnitude}")

import numpy as np

input_file = open("input", "r")
data = []
folds = []

row = input_file.readline().strip()
while row:
    row_split = list(map(int, row.split(',')))
    data.append(row_split)
    row = input_file.readline().strip()
data = np.array(data)

row = input_file.readline().strip()
while row:
    row_split = row.split(" ")
    (direction, at) = row_split[2].split('=')
    folds.append({'dir': direction, 'at': int(at)})
    row = input_file.readline().strip()


def display(data):
    disp = np.full((max(data[:,0])+1, max(data[:,1])+1),'.',dtype=str)
    cnt = np.zeros((max(data[:,0])+1, max(data[:,1])+1), dtype=int)
    for point in data:
        disp[point[0],point[1]] = '#'
        cnt[point[0],point[1]] = 1
    for row in disp:
        print(''.join(list(row)[::-1]))
    return np.sum(cnt)

def foldAt(data, direction, at):
    folded = []
    for point in data:
        if(direction == 'x'):
            if (point[0] < at):
                folded.append(point)
            else:
                folded.append([at - (point[0] - at), point[1]])
        elif(direction == 'y'):
            if (point[1] < at):
                folded.append(point)
            else:
                folded.append([point[0], at - (point[1] - at)])
    return(np.array(folded))

result = data
count = 0
print("ORIGINAL:")
display(data)
for fold in folds:
    print("FOLD AT: ", fold)
    result = foldAt(result, fold['dir'], fold['at'])
    count = display(result)
    print("COUNT: ", count)
    break #oh, only the first fold is the question, ok


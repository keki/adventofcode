import numpy as np
from os import system
from time import sleep

def pixelToInt(pixel):
    if pixel == '.':
        return 0
    else:
        return 1

def intToPixel(int):
    if int == 0:
        return '.'
    else:
        return "#"

def read_input():
    with open('input', 'r') as input_file:
        data = []
        scanner = []
        algo = list(map(pixelToInt,input_file.readline().strip()))
        _ = input_file.readline() # read empty line
        row = input_file.readline().strip()
        image = []
        while row:
            image.append(list(map(pixelToInt, row)))
            row = input_file.readline().strip()
        return (np.array(algo), np.array(image))

def pixel_value(img, pos, outside_bit, algo):
    pv = 0
    for i in -1, 0 , 1:
        for j in -1, 0, 1:
            if (out_of_bounds(img, (pos[0]+i, pos[1]+j))):
                v = outside_bit
            else:
                v = img[pos[0]+i,pos[1]+j]
            pv = pv * 2 + v
    return algo[pv]

def out_of_bounds(arr, pos):
    oob = pos[0] < 0 or pos[1] < 0 or pos[0] >= arr.shape[0] or pos[1] >= arr.shape[1]
    return oob

def img_map(input_image, algo, outside_bit):
    pad = 2
    input_image = np.pad(input_image, pad_width=pad, mode='constant', constant_values=outside_bit)
    outside_arr = np.full((3,3), outside_bit)
    image = np.zeros(input_image.shape, dtype=int)

    new_outside_bit = pixel_value(outside_arr, (1,1), outside_bit, algo)

    for i, row in enumerate(image):
        for j, bit in enumerate(row):
            image[i, j] = pixel_value(input_image, (i,j), outside_bit, algo)

    return (image, new_outside_bit)

def to_string(image):
    def bit_to_hash(bit):
        if(bit == 0):
            return '.'
        else:
            return '#'

    return "\n".join([''.join(list(map(bit_to_hash, row))) for row in image])


def main():
    algo, image = read_input()

    #print(algo)
    #print(to_string(image))

    outside_bit = 0
    for i in range(50):
        (image, outside_bit) = img_map(image, algo, outside_bit)
        print(i)
        #print(to_string(image))

    print("LIT BITS:", np.sum(image))

if __name__ == "__main__":
    main()

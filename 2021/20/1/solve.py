import numpy as np
from os import system


def read_input():
    with open('input', 'r') as input_file:
        algo = list(map(as_int, input_file.readline().strip()))
        _ = input_file.readline()  # read empty line
        row = input_file.readline().strip()
        image = []
        while row:
            image.append(list(map(as_int, row)))
            row = input_file.readline().strip()
        return (np.array(algo), np.array(image))


def as_int(pixel):
    if pixel == '.':
        return 0
    else:
        return 1


def as_char(int):
    if int == 0:
        return '.'
    else:
        return "#"


def bit_value(img, pos, outside_bit, algo):
    pv = 0
    for i in -1, 0, 1:
        for j in -1, 0, 1:
            if (out_of_bounds(img, (pos[0] + i, pos[1] + j))):
                v = outside_bit
            else:
                v = img[pos[0] + i, pos[1] + j]
            pv = pv * 2 + v
    return algo[pv]


def out_of_bounds(arr, pos):
    oob = pos[0] < 0 or pos[1] < 0 \
        or pos[0] >= arr.shape[0] or pos[1] >= arr.shape[1]
    return oob


def img_map(input_image, algo, outside_bit):
    pad = 2
    input_image = np.pad(input_image, pad_width=pad,
                         mode='constant', constant_values=outside_bit)
    outside_arr = np.full((3, 3), outside_bit)
    image = np.zeros(input_image.shape, dtype=int)

    new_outside_bit = bit_value(outside_arr, (1, 1), outside_bit, algo)

    for i, row in enumerate(image):
        for j, bit in enumerate(row):
            image[i, j] = bit_value(input_image, (i, j), outside_bit, algo)

    return (image, new_outside_bit)


def as_string(image):
    return "\n".join([''.join(list(map(as_char, row))) for row in image])


def main():
    algo, image = read_input()

    # print(algo)
    print(as_string(image))

    outside_bit = 0
    for i in range(50):
        (image, outside_bit) = img_map(image, algo, outside_bit)
        system('clear')
        print(as_string(image))

    print("LIT BITS:", np.sum(image))


if __name__ == "__main__":
    main()

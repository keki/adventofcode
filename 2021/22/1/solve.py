import numpy as np

def read_input():
    with open('input', 'r') as input_file:
        data = []
        row = input_file.readline().strip()
        while row:
            (on_off, rest) = row.split(' ', 2)
            xyz = list(map(lambda x: list(map(int, x[2:].split('..'))), rest.split(',')))
            data.append({ "bit": on_off == "on", "cuboid": xyz })
            row = input_file.readline().strip()
        return data

def main():

    # dimensions: x,y,z coordinates + 50
    # value: bit
    state = np.zeros((101,101,101), dtype=bool)

    for command in read_input():
        x_lo = command["cuboid"][0][0]+50
        x_hi = command["cuboid"][0][1]+50
        y_lo = command["cuboid"][1][0]+50
        y_hi = command["cuboid"][1][1]+50
        z_lo = command["cuboid"][2][0]+50
        z_hi = command["cuboid"][2][1]+50
        state[x_lo:x_hi, y_lo:y_hi, z_lo:z_hi] = command["bit"]

    print("RESULT:", np.sum(state))

if __name__ == "__main__":
    main()


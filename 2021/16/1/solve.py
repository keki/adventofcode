import numpy as np

def read_input():
    input_file = open("testinput1", "r")
    row = input_file.readline().strip()
    print(row)
    row_split = list(map(lambda c:c, str(row)))
    return row_split


def as_bits(hexa_digits):
    res = []
    for hexa_digit in hexa_digits:
        res += list(map(int,''.join(bin(int(hexa_digit,16))[2:]).zfill(4)))
    return res

def to_int(bit_repr):
    return int(''.join(list(map(str, bit_repr))),2)

def pop_bits(n):
    global bits
    res = bits[:n]
    bits = bits[n:]
    return res

def pop_bit():
    global bits
    res = bits[0]
    bits = bits[1:]
    return res

def parse_literal(pad = True):
    global bits
    done = True
    res_arr = []
    group_count = 0
    while (done):
        done = pop_bit() # get just one bit
        res_arr += pop_bits(4)
        group_count += 1
    value_length = group_count * 5
    if (pad):
        mod4 = ((6 + value_length) % 4) # header is 6 bits
        if (mod4 != 0):
            ignore_bits = 4 - mod4
            bits = bits[ignore_bits:]
    return to_int(res_arr)

packet_version_sum = 0
def parse_packet(pad = True):
    global packet_version_sum
    # parse header
    packet = {}
    packet['version'] = to_int(pop_bits(3))
    packet_version_sum += packet['version']
    packet['typeID'] = to_int(pop_bits(3))
    packet['subpackets'] = []
    # parse rest depending on typeID
    if (packet['typeID'] == 4):
        packet['value'] = parse_literal(pad)
    else:
        length_type_id = pop_bit()
        if (length_type_id == 0):
            value_length = to_int(pop_bits(15))
            bits_target_length = len(bits) - value_length
            while (bits_target_length < len(bits)):
                packet['subpackets'].append(parse_packet(pad = False))
        else:
            subpacket_count = to_int(pop_bits(11))
            for i in range(0,subpacket_count):
                packet['subpackets'].append(parse_packet(pad = False))

    print(packet)
    #print(bits)
    return packet


bits = as_bits(read_input())
print(bits)
parse_packet()
print(packet_version_sum)

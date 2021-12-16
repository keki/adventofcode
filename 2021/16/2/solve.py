import numpy as np

def read_input():
    input_file = open("input", "r")
    row = input_file.readline().strip()
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

def parse_literal():
    read_more = True
    bits_read = []
    while (read_more):
        read_more = pop_bit() # get just one bit
        bits_read += pop_bits(4)
    return to_int(bits_read)

type_id_to_str = ['sum', 'prod', 'min', 'max', 'value', 'gt', 'lt', 'eq']

def parse_packet():
    # parse header
    packet = {
        'version': to_int(pop_bits(3)),
        'type': type_id_to_str[to_int(pop_bits(3))]
    }
    # parse rest depending on typeID
    if (packet['type'] == 'value'):
        packet['value'] = parse_literal()
    else:
        packet['subpackets'] = []
        length_type_id = pop_bit()
        if (length_type_id == 0):
            # length shows number of bits to read in a 15 bit number
            bits_to_read = to_int(pop_bits(15))
            bits_target_length = len(bits) - bits_to_read
            while (bits_target_length < len(bits)):
                packet['subpackets'].append(parse_packet())
        else:
            # length shows number of subpackets to read in a 11 bit number
            subpacket_count = to_int(pop_bits(11))
            for i in range(0,subpacket_count):
                packet['subpackets'].append(parse_packet())

    return packet

def value(packet):
    def subpacket_values(packet):
        return [value(subpacket) for subpacket in packet['subpackets']]

    if (packet['type'] == 'sum'):
        summa = 0
        for v in subpacket_values(packet):
            summa += v
        return summa
    elif (packet['type'] == 'prod'):
        prod = 1
        for v in subpacket_values(packet):
            prod *= v
        return prod
    elif (packet['type'] == 'min'):
        return min(subpacket_values(packet))
    elif (packet['type'] == 'max'):
        return max(subpacket_values(packet))
    elif (packet['type'] == 'value'):
        return packet['value']
    elif (packet['type'] == 'gt'):
        if (value(packet['subpackets'][0]) > value(packet['subpackets'][1])):
            return 1
        else:
            return 0
    elif (packet['type'] == 'lt'):
        if (value(packet['subpackets'][0]) < value(packet['subpackets'][1])):
            return 1
        else:
            return 0
    elif (packet['type'] == 'eq'):
        if (value(packet['subpackets'][0]) == value(packet['subpackets'][1])):
            return 1
        else:
            return 0


def asString(packet):
    def subpacket_strings(packet):
        return [asString(subpacket) for subpacket in packet['subpackets']]

    if (packet['type'] == 'sum'):
        summa = []
        for v in subpacket_strings(packet):
            summa.append(v)
        return "(" + " + ".join(summa) + ")"
    elif (packet['type'] == 'prod'):
        prod = []
        for v in subpacket_strings(packet):
            prod.append(v)
        return "(" + " * ".join(prod) + ")"
    elif (packet['type'] == 'min'):
        return "min(" + ', '.join(subpacket_strings(packet)) + ")"
    elif (packet['type'] == 'max'):
        return "max(" + ', '.join(subpacket_strings(packet)) + ")"
    elif (packet['type'] == 'value'):
        return str(packet['value'])
    elif (packet['type'] == 'gt'):
        return str(value(packet['subpackets'][0])) + " > " + str(value(packet['subpackets'][1]))
    elif (packet['type'] == 'lt'):
        return str(value(packet['subpackets'][0])) + " < " + str(value(packet['subpackets'][1]))
    elif (packet['type'] == 'eq'):
        return str(value(packet['subpackets'][0])) + " == " + str(value(packet['subpackets'][1]))

bits = as_bits(read_input())
code = parse_packet()
print(asString(code), ' === ', value(code))

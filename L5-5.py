# python lab 5 10-6-20

# l5_5 125 << 4 (shift left four bits,  same as *16)

def print_padded_byte(b):
    print(bin(b)[2:].rjust(8, '0'))


print_padded_byte(125)


print(125 << 4)

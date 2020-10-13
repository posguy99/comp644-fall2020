# python lab 5 10-6-20

# l5_4 125 << 2 (shift left two bits,  same as *4)

def print_padded_byte(b):
    print(bin(b)[2:].rjust(8, '0'))


print_padded_byte(125)


print(125 << 2)

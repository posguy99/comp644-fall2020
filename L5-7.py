# python lab 5 10-6-20

# l5_7 1024 >> 4 (shift right two bits,  same as /16)

def print_padded_byte(b):
    print(bin(b)[2:].rjust(8, '0'))


print_padded_byte(1024)


print(1024 >> 4)

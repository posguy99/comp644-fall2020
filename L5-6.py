# python lab 5 10-6-20

# l5_6 1024 >> 2 (shift right two bits,  same as /4)

def print_padded_byte(b):
    print(bin(b)[2:].rjust(8, '0'))


print_padded_byte(1024)


print(1024 >> 2)

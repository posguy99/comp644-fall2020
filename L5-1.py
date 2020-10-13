# python lab 5 10-6-20

# l5_1 31&14 (and)

def print_padded_byte(b):
    print(bin(b)[2:].rjust(8, '0'))


print_padded_byte(31)
print_padded_byte(14)

print(31 & 14)

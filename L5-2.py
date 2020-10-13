# python lab 5 10-6-20

# l5_2 60|14 (or)

def print_padded_byte(b):
    print(bin(b)[2:].rjust(8, '0'))


print_padded_byte(60)
print_padded_byte(14)

print(60 | 14)

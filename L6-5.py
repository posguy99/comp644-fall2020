
# L6-5

# note that this does not avoid divide by zero

def mod(x, y):
    return x % y


tup1 = (100, 25, 10, 5, 1)
lst2 = [each for each in range(100, 151)]

for each in lst2:
    print('-----', each, '-----')
    for item in tup1:
        print(each, '\tMod', item, '\t', mod(each, item))

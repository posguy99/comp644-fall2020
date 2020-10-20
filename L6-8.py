
# L6-8

# note that this does not avoid divide by zero

import L6_7m

tup1 = (100, 25, 10, 5, 1)
lst2 = [each for each in range(100, 151)]

for each in lst2:
    print('-----', each, '-----')
    for item in tup1:
        print(each, '\tMod', item, '\t', L6_7m.mod(each, item))
        print(each, '\tFloor', item, '\t', L6_7m.floor(each, item))

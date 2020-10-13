# python lab 5 10-6-20

# l5_15

from random import randint

the_list = [[randint(1, 20) for each in range(4)]for item in range(3)]

print('the_list: ', the_list)

# tricksy because indexes start at *zero*
print('Second element of the second list is', the_list[1][1])

# challenge 5_1

for i in range(3):
    for j in range(4):
        print(the_list[i][j], '\t', end='')
    print()

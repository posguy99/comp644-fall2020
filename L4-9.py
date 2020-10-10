# L4_9​. Reverse the list created in L4_8

from random import randint

theList = [randint(1, 6) for x in range(6)]

print('Unreversed list: ', theList)
theList.reverse()
print('Reversed list: ', theList)

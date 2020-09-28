# append values 50 to 75 to list created L3_2.

theList = list()
theList = [each for each in range(1, 31, 1)]

print('begin theList: ', theList)

# now append...

for i in range(50, 76, 1):
    theList.append(i)

print('end theList: ', theList)

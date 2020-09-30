# Delete item equal to 201 in list created in L3_7.


theList = list()
theList = [each for each in range(1, 31, 1)]

print('begin theList: ', theList)

# now append...

for i in range(50, 76, 1):
    theList.append(i)

print('after append, before insert theList: ', theList)

# making sure to point out that this is going to insert the numbers in reverse
# order since it's always inserting at the first position

for i in range(200, 226, 1):
    theList.insert(0, i)

print('after insert theList: ', theList)

for each in range(len(theList)):
    if theList[each] == 201:
        theList.pop(each)
        break

# 201 is now missing from theList

print('after pop 201 theList: ', theList)

# Walk the list created in L3_2 and if the value is 10 stop the loop.

theList = list()
theList = [each for each in range(1, 31, 1)]

print(theList)

for each in theList:

    if each == 10:
        print('Came to 10')
        break
    else:
        print(each, end=' ')

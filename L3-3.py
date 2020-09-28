# walk the list created in L3_2 using a while loop and print the value
# except if they are 5, 25 and 17


theList = list()
theList = [each for each in range(1, 31, 1)]
theMatch = [5, 17, 25]

print(theList)

for each in theList:
    if each in theMatch:        # saves a bunchtillion if/elif/else
        continue
    else:
        print(each, end=' ')

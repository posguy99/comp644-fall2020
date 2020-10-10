# L4_6.​ Create a list and then sort the list.

theList = list()

while True:
    user_input = int(input('Enter a number between 1 and 100, or 0 to end: '))
    if user_input == 0:
        break
    if (user_input < 0) or (user_input > 100):
        print('Invalid, input must be between 1 and 100!')
        continue
    theList.append(user_input)

print('theList unsorted: ', theList)
theList.sort()
print('theList sorted: ', theList)

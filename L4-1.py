# L4_1.​ Write a program that asks for user input of a number.
# The program should ask the user to input numbers until the user
# wants to stop. The number must be between 1 and 100 and the program
# stops if the user inputs a 0. The values a user inputs should be stored
# in a Python list and when the user finishes entering numbers and exits
#  the list should be printed.

theList = list()

while True:
    user_input = int(input('Enter a number between 1 and 100, or 0 to end: '))
    if user_input == 0:
        break
    if (user_input < 0) or (user_input > 100):
        print('Invalid, input must be between 1 and 100!')
        continue
    theList.append(user_input)
print('theList: ', theList)

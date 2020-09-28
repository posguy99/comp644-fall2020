# Create a while loop that will repetitively ask for a number.
# If the number entered is 9999 stop the loop.

while True:
    answer = int(input('Enter a number, 9999 to end: '))
    if answer == 9999:
        break
    else:
        print('Your number was: ', answer)

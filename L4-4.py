# L4_4.​ The mathematical integer division is used to calculate how many times
# a value is divisible by another value.
# As an example, 100 integer division 25 is 4
# (Python represents this calculation as 100//25)
# and 102 integer division 25 is 4. # Any remainder is ignored (see L4_5).
# Write a function that takes two values as parameters and returns
# the calculation of integer division from the two values.


def integer_division(a, b):
    ''' divide a by b, return the integer result '''
    return a // b


print('Divide 100 by 25, result is: ', integer_division(100, 25))
print('Divide 102 by 25, result is: ', integer_division(102, 25))

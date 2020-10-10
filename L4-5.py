# The mathematical modulo is used to calculate the remainder of the
# integer division. As an example, 102%25 is 2.
# Write a function that takes two values as parameters and returns
# the calculation of a modulo from the two values.

def mathematical_modulo(a, b):
    ''' divide a by b, return the remainder '''
    return a % b


print('Divide 100 by 25, remainder is: ', mathematical_modulo(100, 25))
print('Divide 102 by 25, remainder is: ', mathematical_modulo(102, 25))

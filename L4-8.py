# L4_8.​ Write a program that populates a list using list comprehension
# of 6 elements using random integers between 1 to 6.

from random import randint

theList = [randint(1, 6) for x in range(6)]

print(theList)

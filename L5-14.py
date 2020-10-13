# python lab 5 10-6-20

# l5_13 deepcopy of a list, the id() are different indicating
# that they do not point to the same list object

from copy import deepcopy

the_list = ['Apples', 'Pears', 'Oranges', 'Mangoes', 'Tomatoes']


print('the_list: ', the_list)
the_new_list = deepcopy(the_list)

print('the_new_list: ', the_new_list)

print('the_list', id(the_list))
print('the__new_list', id(the_new_list))

# python lab 5 10-6-20

# l5_13 shallow copy of a list, the id() are the same indicating
# that they are both pointers to the same list object

the_list = ['Apples', 'Pears', 'Oranges', 'Mangoes', 'Tomatoes']


print('the_list: ', the_list)
the_new_list = the_list

print('the_new_list: ', the_new_list)

print('the_list', id(the_list))
print('the__new_list', id(the_new_list))


# L6-2

list = [each for each in range(1980, 2020)]
print(list)
for each in list:
    if each % 4 == 0:
        result = True
    else:
        result = False

    print(each, '\t', result)

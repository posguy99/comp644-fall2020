# Rewrite of L14-12

list = [each for each in range(1980, 2020)]
print(list)
for each in list:
    result = True if (each % 4 == 0) else False
    print(each, '\t ', result)

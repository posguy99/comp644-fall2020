# L4_11. After executing the following Python script observe the results:

for each in range(1980, 2020):
    if each % 4 == 0:
        result = True
    else:
        result = False

    print(each, '\tLeap Year?\t ', result)

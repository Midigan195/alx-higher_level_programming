#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    number = ""
    if x <= 0:
        return 0
    for i in range(0, x):
        try:
            number = number + str(my_list[i])
        except IndexError:
            i -= 1
            break
    print("{}" .format(number))
    return i + 1

#!/usr/bin/python3
uniq_add = __import__('2-uniq_add').uniq_add

my_list = [1, 2, 3, 1, 4, 2, 6, 6, 6, 6, 6, 6, 5, 2, 2, 2, 2]
result = uniq_add(my_list)
print("Result: {:d}".format(result))

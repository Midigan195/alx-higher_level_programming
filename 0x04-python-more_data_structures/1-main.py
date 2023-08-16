#!/usr/bin/python3
search_replace = __import__('1-search_replace').search_replace

my_list = [1, 1, 12]
new_list = search_replace(my_list, 1, 78)

print(new_list)
print(my_list)

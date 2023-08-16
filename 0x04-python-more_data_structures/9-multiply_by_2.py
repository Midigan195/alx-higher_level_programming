#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    cp = a_dictionary.copy()
    for x in a_dictionary:
        cp[x] = cp[x] * 2
    return cp

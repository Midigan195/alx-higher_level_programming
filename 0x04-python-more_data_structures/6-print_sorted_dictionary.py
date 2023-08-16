#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a = a_dictionary
    {x: print("{}: {}".format(x, a[x])) for x in sorted(a)}

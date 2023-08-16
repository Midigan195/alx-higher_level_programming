#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    new_dict = a_dictionary.copy()
    if key in a_dictionary:
        a_dictionary.pop(key)
        new_dict.pop(key)
    return new_dict

#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_dict = a_dictionary.copy()
    new_dict.update({key: value})
    a_dictionary.update({key: value})
    return new_dict

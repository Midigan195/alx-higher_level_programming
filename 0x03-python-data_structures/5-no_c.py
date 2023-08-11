#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    text = list(my_string)
    for c in text:
        if c != "c" and c != "C":
            new_str += c
    return new_str

#!/usr/bin/python3
def print_last_digit(number):
    c = str(number)
    print("{}".format(c[-1]), end="")
    c = int(c[-1])
    return c

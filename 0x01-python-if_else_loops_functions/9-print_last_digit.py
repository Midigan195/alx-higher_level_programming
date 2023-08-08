#!/usr/bin/python3
def print_last_digit(number):
    c = str(number)
    print("{}".format(c[-1]), end="")

    return int(c[-1])

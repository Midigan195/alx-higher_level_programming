#!/usr/bin/python3
def uppercase(str):
    for c in str:
        i = ord(c)
        if i >= 97 and i <= 122:
            c = chr(i - 32)
        print("{}".format(c), end="")
    else:
        print()

#!/usr/bin/python3
def fizzbuzz():
    s = ""
    for i in range(1,101):
        if i % 3 == 0:
            s = "Fizz"
            if i % 5 == 0:
                s = s + "Buzz"
        elif i % 5 == 0:
            s = "Buzz"
        else:
            s = i
        print("{} ".format(s), end="")

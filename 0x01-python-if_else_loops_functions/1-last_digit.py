#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = str(number)[-1]
s = ""
if number < 0:
    last = "-" + last
if int(last) > 5:
    s += "and is greater than 5"
elif int(last) == 0:
    s += "and is 0"
elif int(last) < 6 and int(last) != 0:
    s += "and is less than 6 and not 0"
print("Last digit of {} is {} {}".format(number, last, s))

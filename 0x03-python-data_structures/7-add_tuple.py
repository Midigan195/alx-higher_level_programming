#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a)
    b = list(tuple_b)
    c = 0
    if len(a) < 2:
        while len(a) != 2:
            a.append(0)
    if len(b) < 2:
        while len(b) != 2:
            b.append(0)
    n = [a[0] + b[0], a[1] + b[1]]
    return tuple(n)

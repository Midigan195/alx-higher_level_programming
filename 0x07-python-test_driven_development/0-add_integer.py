#!/usr/bin/python3
"""
This module includes a function that adds two integers

The module contains a function that adds two integers
"""


def add_integer(a, b=98):
    """
    add_integer functions adds the values of 2 integers and returns the result
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b

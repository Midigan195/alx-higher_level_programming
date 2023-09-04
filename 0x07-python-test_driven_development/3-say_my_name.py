#!/usr/bin/python3
"""
This module contains a function that prints a fist and last names

This module has a function that prints a string followed by name and last name
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name prints My name is followed by the first_name and last_name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

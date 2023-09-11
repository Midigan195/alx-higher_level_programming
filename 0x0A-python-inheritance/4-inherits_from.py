#!/usr/bin/python3
"""
This module has a function that finds wether an objects is of a specific class.

This module has one function that determines
if an instace is of a specified class.
"""


def inherits_from(obj, a_class):
    """
    This function determines if an instance if of a specific class.

    Args:
        obj: The object to test.
        a_class: The class to test against.
    Returns:
        True if object is a instance of class or subclass else False.
    """
    return issubclass(type(obj), a_class)

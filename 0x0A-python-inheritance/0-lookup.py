#!/usr/bin/python3
"""
This module contains a function that lists
the available objects and methods.

The module contains one function that prints a list of methods and attributes.
"""


def lookup(obj):
    """
    This function returns a list of methods and attributes
    associated with an object.

    Args:
        obj: The object to look at.

    Returns:
        List of methods and attributes.
    """
    return dir(obj)

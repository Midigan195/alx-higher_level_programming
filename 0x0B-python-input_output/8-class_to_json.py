#!/usr/bin/python3
"""
This module has a function that returns an objects dictionary discription

This module has one function that returns a dictionary desription of an object
"""


def class_to_json(obj):
    """
    This class test if an object can be converted in json format

    This class checks wether obj is a str, int, bool, list or dict
    and returns it

    Args:
        obj (object): object to test for serialisation

    Returns:
        dictionary description with simple data structure.
    """
    if isinstance(obj, (str, int, bool, list, dict)):
        return obj
    elif hasattr(obj, '__dict__'):
        return obj.__dict__

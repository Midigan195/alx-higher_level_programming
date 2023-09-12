#!/usr/bin/python3
"""
This module defines a function that converts a json string to object

This module contains one function that converts a json string to object
"""
import json


def from_json_string(my_str):
    """
    Returns a object from json string

    Args:
        my_str (string): Name of string to be deserialised

    Returns:
        deserialised representation of object
    """
    return json.loads(my_str)

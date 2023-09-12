#!/usr/bin/python3
"""
This module defines a function that converts an object to json

This module contains one function that converts an object to json
"""
import json


def to_json_string(my_obj):
    """
    Returns a json representation of my_obj

    Args:
        my_obj (object): Name of object to be serialised

    Returns:
        Serialised representation of object
    """
    return json.dumps(my_obj)

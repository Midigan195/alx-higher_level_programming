#!/usr/bin/python3
"""
This module defines a function that writes an object to a textfile

This module contains one function that writes an object to a textfile
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to specified textfile

    Args:
        my_obj (object): Name of object to write to
        filename (file): Name of file to be written to
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)

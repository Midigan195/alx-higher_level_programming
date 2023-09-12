#!/usr/bin/python3
"""
This module defines a function that creates an object from a json file

This module contains one function that creates an object from a json file
"""
import json


def load_from_json_file(filename):
    """
    Returns a object from json file

    Args:
        filename (file): Name of file to be converted

    Returns:
        Deserialised object
    """
    with open(filename, 'r') as f:
        return json.load(f)

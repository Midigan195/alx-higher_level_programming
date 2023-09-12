#!/usr/bin/python3
"""
This module defines a function that appends to a textfile

This module contains one function that appends text into a textfile
"""


def append_write(filename="", text=""):
    """
    Appends text into a textfile of filename.
    If the file does not exist create a new file.

    Args:
        filename (str, optional): Name of file to be appended to.
        Defaults to empty string.
        text (str, optional): Text to be appended to file.
        Defaults to empty string.

    Returns:
        (int): Number of characters appended

    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)

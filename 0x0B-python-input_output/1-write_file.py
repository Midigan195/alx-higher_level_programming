#!/usr/bin/python3
"""
This module defines a function that writes to a textfile

This module contatins one function that writes text into a textfile
"""


def write_file(filename="", text=""):
    """
    Writes text into a textfile of filename.
    If the file does not exist create a new file.

    Args:
        filename (str, optional): Name of file to be written to.
        Defaults to empty string.
        text (str, optional): Text to be written to file.
        Defaults to empty string.

    Returns:
        (int): Number of characters written

    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)

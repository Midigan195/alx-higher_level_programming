#!/usr/bin/python3
"""
This module defines a function that prints the contents of a file

This module contains one function that prints the contents of a textfile
"""


def read_file(filename=""):
    """
    Prints all contents of a textfile to standard output

    Args:
        filename (str, optional): Name of the file to be read.
        defaults to empty textfile name
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print((f.read()).strip())

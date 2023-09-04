#!/usr/bin/python3
"""
This module contains a function that prints a string

This module has one function that prints text to the terminal
"""


def text_indentation(text):
    """
    text_indentation prints a string that is correctly indented
    """
    line = ""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    for c in range(0, len(text)):
        line = line + text[c]
        if text[c] in [".", "?", ":"] and c != len(text) - 1:
            line = line.strip()
            print(line)
            print()
            line = ""
        elif c == len(text) - 1:
            line = line.strip()
            print(line, end="")

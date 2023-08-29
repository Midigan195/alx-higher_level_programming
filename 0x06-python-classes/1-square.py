#!/usr/bin/python3
"""Defines a square class.

This module contains a square class,
which represents a sqaure with an attribute for its size.

Classes:
    Square
"""


class Square:
    """Represents a square shape.

    This provides a basic representation of a square
    with an attribute for size.

    Attributes:
        __size: The size of each side of the square
    """
    def __init__(self, size):
        """Initialization of Square instance

        Args:
            size: The size of each side of the square
        """
        self.__size = size

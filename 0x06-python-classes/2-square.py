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
    def __init__(self, size=0):
        """Initialization of Square instance.

        Args:
            size (int, optional): The size of each side of the square.
            0 by default.

        Raises:
            TypeError: If size is not integer
            ValueError: If size is < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

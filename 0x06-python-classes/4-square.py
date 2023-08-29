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
        """
        self.__size = size

    @property
    def size(self):
        """Getter method returns the size value

        Returns:
            size of the instance
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method sets size of square

        Args:
            value (int): size of the square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size < 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of square by squaring the size.

        Returns:
            Area of square instance.
        """
        return self.__size ** 2

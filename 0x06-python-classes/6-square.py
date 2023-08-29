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
        __position: The position of the square in the x and y coordinates
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialization of Square instance.

        Args:
            size (int, optional): The size of each side of the square.
            0 by default.
            position: (tuple, optional): Position of square.
            (0, 0) by default.
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Getter method returns the position of square

        Returns:
            position of instance
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method sets position of square

        Args:
            value: position of square

        Raises:
        TypeError: If value is not a tuple with 2 positive integers
        """
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
                    return
        raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Calculates the area of square by squaring the size.

        Returns:
            Area of square instance.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints a sqaure of # with each side eqaul
        to the size of square instance
        """
        if self.__size == 0:
            print()
        if not self.__position[1] > 0:
            for i in range(0, self.__position[1]):
                print()
        for i in range(0, self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

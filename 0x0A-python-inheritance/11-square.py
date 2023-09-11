#!/usr/bin/python3
"""
This module define a Square that inherits from Rectangle.

This module contains one class, Square, which inherits
attrinutes and methds from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a sqaure.

    This class creates an instance representation of a square.
    """
    def __init__(self, size):
        """
        Initialise Square instance

        Args:
            size (int): width of square.
        """
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculate the area of the sqaure

        Returns:
            int: area of the sqaure
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string reprsenttation of sqaure

        Returns:
            str: string representation of sqaure
        """
        return "[Square] {}/{}" .format(self.__size, self.__size)

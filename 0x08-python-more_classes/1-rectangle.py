#!/usr/bin/python3
"""
This module contains a class that defines a rectangle

This module has a class called Rectangle
that has a specified height and width
"""


class Rectangle:
    """
    Reprsentation of a rectangle with a specific width and height

    Rectangle defines width and heigh represntations of the dimensions
    of a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initilises rectangle with a specific width and height

        Args:
            width (int, optional): The width of the rectangle
            height (int, optional): The heigh of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """
        Getter returns height private attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter sets value to height if it in an integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """
        Getter returns width private attribute
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Setter sets value to width if it in an integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

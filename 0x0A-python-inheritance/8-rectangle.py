#!/usr/bin/python3
"""
This module define a rectangle that inherits from Base geometry.

This module contains one class, Rectangle, which inherits
attrinutes and methds from base geomrtry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle.

    This class creates an instance representation of a rectangle.
    """
    def __init__(self, width, height):
        """
        Initialise rectangle instance

        Args:
            width (int): width of rectangle.
            height (int): height of rectangle.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

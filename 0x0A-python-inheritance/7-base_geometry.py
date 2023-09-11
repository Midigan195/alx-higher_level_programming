#!/usr/bin/python3
"""
This module define a geometry related class

This module has one class called base geometry with
with an area function
"""


class BaseGeometry:
    """
    An empty base class for geomrtry related classes

    This class is a base for other classes
    """
    def area(self):
        """
        This function raises an exception message

        Raises:
            Exception: if area method is called
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This function validates the functions name and value

        Args:
            name: name to be evaluated
            value: integers to be evaluated
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer". format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0". format(name))

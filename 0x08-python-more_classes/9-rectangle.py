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

    Attributes:
        number_of_instances (int): Total number of rectangles
        print_symbol: Item to represent rectangle class
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initilises rectangle with a specific width and height

        Args:
            width (int, optional): The width of the rectangle
            height (int, optional): The heigh of the rectangle
            print_symbol: Item to represent rectange instance
        """
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """
        Getter returns height private attribute

        Returns:
            Height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter sets value to height if it in an integer

        Args:
            value: height of rectangle

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is < 0
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

        Returns:
            Width of rectangle
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Setter sets value to width if it in an integer

        Args:
            value: width of rectangle

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """
        Calculates the area of a rectangle and returns the result
        """
        return self.__height * self.__width

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Checks wich rectangle is bigger

        Args:
            rect_1 (): Recatngle 1
            rect_2 (): Rectangle 2

        Raises:
            TypeError: if both rect_1 and rect_2 are instances of Rectangle

        Returns:
            Bigger of the two rectangles
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """
        Creates a new rectangle instance with all dimensions = size

        Args:
            size (int, optional): sizr of the rectangle

        Returns:
            new rectangle object
        """
        return cls(size, size)

    def perimeter(self):
        """
        Calculates the perimeter of rectangle and returns the result
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """
        Returns a string representation of rectangle

        Returns:
            rect_shape (str): string representation of specific rectangle
        """
        rect_shape = ""
        s = str(self.print_symbol)
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(1, self.__height):
            rect_shape = rect_shape + (s * self.__width) + "\n"
        else:
            rect_shape = rect_shape + (s * self.__width)
        return rect_shape

    def __repr__(self):
        """
        Returns string representation of rectangle that can be used with eval
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a message on rectangle deletion
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

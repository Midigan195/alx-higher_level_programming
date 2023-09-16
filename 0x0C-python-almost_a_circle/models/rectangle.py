#!/usr/bin/python3
"""
This module defines a class that represents a rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    This class defines a rectangle that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initilises all definitions associated with rectangle

        Args:
            width: width of rectangle instance
            height: the height of rectangle instance
            x: the x position of instance
            y: the y position
            id: id number of instance
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Gets the width of rectangle and returns it
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of rectangle to value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of rectangle and returns it
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of rectangle to value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Gets the x value of rectangle to return
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the x value of rectangle to value
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Gets the y value oif rectangle and returns
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the y value of rectangle to value
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Returns the area of rectangle instance
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints a string representation of rectangle instance
        """
        for j in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def to_dictionary(self):
        """
        Return dictionary formated for json serilization
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """
        Returns a formated string of the rectangle instance
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format
                (self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """
        Update the arguments in rectangle instance with new values
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for n, a in kwargs.items():
                if hasattr(self, n):
                    setattr(self, n, a)

#!/usr/bin/python3
"""
This module defines a class that represents a sqaure inherited
from the rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class defines a representation of a sqaure
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialisation of the specification of a sqaure
        inherited from rectangle

        Args:
            size: size of sqaure instance
            x: x position of sqaure instance
            y: y position of sqaure instance
            id: Id of sqaure instance
        """
        super().__init__(size, size, x, y, id)
        self.__size__ = size

    @property
    def size(self):
        """
        Getter returns size of square instance
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter sets size of square instance
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the arguments in square instance with new values
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for n, a in kwargs.items():
                if hasattr(self, n):
                    setattr(self, n, a)

    def to_dictionary(self):
        """
        Return string formated dictionary for json serilization
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """
        Returns a formated string of the sqaure instance
        """
        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.size))

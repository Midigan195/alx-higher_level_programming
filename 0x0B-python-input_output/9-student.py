#!/usr/bin/python3
"""
This module contains a class that is a representation of a student

This module has on class that represents a student and thier attributes
"""


class Student:
    """
    This class defines the attributes of a student

    This class represents a student and thier attributes
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialisation for the fist name last name and age

        Args:
            first_name: students first name
            last_name: students last name
            age: students age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Converts the attributes of students for json serialisation

        Returns:
            dictionary of attributes of student
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }

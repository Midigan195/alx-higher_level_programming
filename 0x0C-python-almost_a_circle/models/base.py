#!/usr/bin/python3
"""
This module defines a class that serves as a base for different shapes
"""
import json


class Base:
    """
    This class defines a base for various shapes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialises id if id is not None to keep track of instance

        Args:
            id (int, optional): id number of instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns json string representation of list_dictionaries
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @staticmethod
    def from_json_string(json_string):
        """
        Returns a list of string in json representation
        """
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        with open(str(cls.__name__) + ".json", "w") as f:
            if list_objs:
                json_list = [i.to_dictionary() for i in list_objs]
                f.write(Base.to_json_string(json_list))
            else:
                f.write("[]")

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a new instance of a class and sets them with values
        """
        new_instance = cls(1, 1)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """
        Create a new instance from a loaded file
        """
        try:
            with open(str(cls.__name__) + ".json", "r") as f:
                dict_list = cls.from_json_string(f.read())
                return [cls.create(**d) for d in dict_list]
        except FileNotFoundError:
            return[]

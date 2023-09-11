#!/usr/bin/python3
"""
This module contains a class that prints a sorted list

This module has one class that inherits the attributes and
propeties of the list class
"""


class MyList(list):
    """
    This class prints a sorted list

    This class has one function that prints a sorted list
    """
    def print_sorted(self):
        """
        This function prints a sorted list in accending order

        Returns:
            None
        """
        print(sorted(self))

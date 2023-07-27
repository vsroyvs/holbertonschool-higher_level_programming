#!/usr/bin/python3
"""Defines an empty class"""


class BaseGeometry():
    """This represent a base geometry"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """this method will validate a parameter as an int
        Args:
            name (str): name of parameter
            value (int): parameter to validate
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

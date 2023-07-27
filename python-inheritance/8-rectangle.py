#!/usr/bin/python3
"""This is a module for rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This is a class Rectangle"""

    def __init__(self, width, height):
        """This is a Constructor.
        Args:
            width: of Rectangle
            height: of Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

#!/usr/bin/python3
"""This is a module for rectangle"""


class Rectangle:
    """This is a class Rectangle"""

    def __init__(self, width=0, height=0):
        """This is a Constructor.
        Args:
            width: of Rectangle
            height: of Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get/ set width atributte"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get/ set height atributte"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

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

    def area(self):
        """This method returns the area of Rectangule"""
        return self.__width * self.__height

    def __str__(self):
        """print() and str() of rectangle description"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string

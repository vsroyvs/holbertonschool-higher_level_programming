#!/usr/bin/python3
"""This is a module for square"""


class Square:
    """This is a class Square"""

    def __init__(self, size=0):
        """This is a Constructor.
        Arguments:
            Size: side of square
        """
        self.size = size

    @property
    def size(self):
        """ These are a getter and setter when to get/set
        the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            # check if size is a int - it returns true or false
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This method returns the area of the square"""
        return (self.__size * self.__size)

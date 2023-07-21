#!/usr/bin/python3
"""This is a module for square"""


class Square:
    """This is a class Square"""

    def __init__(self, size=0):
        """This is a Constructor.
        Arguments:
            Size: side of square
        """
        if not isinstance(size, int):
            # check if size is a int - it returns true or false
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

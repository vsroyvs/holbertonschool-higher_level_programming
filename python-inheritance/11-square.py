#!/usr/bin/python3
"""This is a module for Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This is a class Square that inherits from Rectangle"""

    def __init__(self, size):
        """this is a constructor.
        Args:
            size: is the measure of the side of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

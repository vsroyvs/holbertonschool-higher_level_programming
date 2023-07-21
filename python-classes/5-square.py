#!/usr/bin/python
"""this is a module for square"""


class Square():
    """this is a Class Square"""
    def __init__(self, size=0):
        """This is a Constructor
        Arguments:
            Size: side of square
        """
        self.size = size

    @property
    def size(self):
        """These are getter and setter whose to get/set
        the curret size of the square"""
        self.__size = size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This is a method that returns the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """This is a method that prints the square with caracter #"""
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")

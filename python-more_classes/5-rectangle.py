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

    def area(self):
        """This public instance method returns the area of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * self.__height)

    def perimeter(self):
        """This public instance method returns perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width*2 + 2*self.__height)

    def __str__(self):
        """Return a representation of rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = []
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append('#')
            if i != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """Return a string that represents of the Rectangle"""
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return rectangle

    del __del__(self):
        """Print a message when each Rectangle is deleted"""
        print("Bye rectangle...")

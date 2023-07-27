#!/usr/bin/python3
"""Defines a object is instance a class"""


def inherits_from(obj, a_class):
    """function that checks an object is instance or class
    Args:
        obj (any): Object
        a_class (type): Class
    Returns:
        True: If is instance of a_class
        False: If is not instance of a_class
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class

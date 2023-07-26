#!/usr/bin/python3
"""Defines a class and inherited class"""


def is_kind_of_class(obj, a_class):
    """function that checks an object is instance or inherited or class
    Args:
        obj (any): Object
        a_class (type): Class
    Returns:
        True: If is instance of a_class
        False: If is not instance of a_class
    """
    return isinstance(obj, a_class)

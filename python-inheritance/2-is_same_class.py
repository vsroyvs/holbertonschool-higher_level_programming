#!/usr/bin/python3
"""Module that determine is a object is exactly an instance of class"""


def is_same_class(obj, a_class):
    """function that checks an object is instance of object
    Args:
        obj (any): Object
        a_class (type): Class
    Returns:
        True: If is instance of a_class
        False: If is not instance of a_class
    """
    if type(obj) == a_class:
        return True
    return False

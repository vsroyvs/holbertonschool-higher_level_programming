#!/usr/bin/python
# 0-add_integer.py
""" Define an addition between two integers"""


def add_integer(a, b= 98):
    """Retruns the integer addition of a and b
    If args are float these must be to casted to integers
    Raises:
        TypeError: If a or b are a not integer or not float.

    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)
    return a + b

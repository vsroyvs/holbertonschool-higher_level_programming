#!/usr/bin/python3
"""SubClass Mylist of Class list"""


class MyList(list):
    """SubClass Mylist of Super Clas list"""

    def print_sorted(self):
        """Returns: a sorted list"""
        print(sorted(self))

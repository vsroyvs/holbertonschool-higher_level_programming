#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """this is a class student."""

    def __init__(self, first_name, last_name, age):
        """Constructor to new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.
        If attrs is a list of strings, represent only those attributes
        Args:
            Attrs (list) :
        """
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of Student
        Args:
            json (dict):
        """
        for k, v in json.items():
            setattr(self, k, v)

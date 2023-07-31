#!/usr/bin/python3
"""Define convert string of Json function"""
import json


def from_json_string(my_str):
    """returns the objest representation of an Json
    Args:
        my_str: obj to will be convert
    """
    return json.loads(my_str)

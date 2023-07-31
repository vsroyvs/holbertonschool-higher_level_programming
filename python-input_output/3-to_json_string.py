#!/usr/bin/python3
"""Define convert json of string function"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object(str)
    Args:
        my_obj: obj to will be convert
    """
    return json.dumps(my_obj)

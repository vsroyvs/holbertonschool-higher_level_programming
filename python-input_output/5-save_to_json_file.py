#!/usr/bin/python3
"""Define a Json file-writing function"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text as a Json representation"""
    with open(filename, 'w') as archive:
        return json.dump(my_obj, archive)

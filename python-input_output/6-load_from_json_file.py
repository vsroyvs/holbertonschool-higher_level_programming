#!/usr/bin/python3
"""Define a Json file-reading function"""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename) as archive:
        return json.load(archive)

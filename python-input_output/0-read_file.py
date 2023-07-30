#!/usr/bin/python3
"""Define file-reading function"""


def read_file(filename=""):
    """ Print the contents of a UTF8 text"""
    with open(filename, encoding="utf-8") as archive:
        content = archive.read()
    print(content, end="")

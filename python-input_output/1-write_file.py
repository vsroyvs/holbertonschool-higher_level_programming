#!/usr/bin/python3
"""Define file-writting function"""


def write_file(filename="", text=""):
    """ write a string to a text file utf8
    Args:
        filename (str): name of file
        text (str): test to write to the file
    """
    with open(filename, 'w', encoding="utf-8") as archive:
        return archive.write(text)

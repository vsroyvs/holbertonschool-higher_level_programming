#!/usr/bin/python3
"""Define file-appending function"""


def append_write(filename="", text=""):
    """ appends a string at the end of text file utf8
    Args:
        filename (str): name of file
        text (str): text to add to the file
    """
    with open(filename, 'a', encoding="utf-8") as archive:
        return archive.write(text)

#!/usr/bin/python3
"""Defines a function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF8)

    Args:
        filename (str): name of the file to append to
        text (str): string to be append at the end of the file
    Returns:
        Number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

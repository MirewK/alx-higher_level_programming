#!/usr/bin/python3
"""Defines a function that writes a string to a textfile"""


def write_file(filename="", text=""):
    """
    Writes a string to a textfile (UTF8).

    Args:
        filename (str): name of the file to be written
        text (str): text to be written in the file
    Returns:
        Number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert text after each line containing a given string

    Args:
        filename (str): name of the file
        search_string (str): string to search for within the file
        new_string (str): string tobe inserted
    """
    txt = ""
    with open(filename) as r:
        for line in r:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as w:
        w.write(txt)

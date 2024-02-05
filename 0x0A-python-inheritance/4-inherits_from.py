#!/usr/bin/python3
"""Defines a function that checks an inherited class"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an inherited instance of a class.

    Args:
        obj (any): object to be checked
        a_class (type): class type to be mached with object
    Returns:
        True if obj is an inherited instance of a_class
        False otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

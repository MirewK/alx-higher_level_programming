#!/usr/bin/python3
"""Defines a function that check if object is exactly an instance"""


def is_same_class(obj, a_class):
    """
    Return True if an object is exactly an instance of a class

    Args:
        obj (any): object to be checked
        a_class (type): class type to be matched with object
    Returns:
        True if obj is exactly an instance of a_class
        False otherwise
    """
    if type(obj) == a_class:
        return True
    return False

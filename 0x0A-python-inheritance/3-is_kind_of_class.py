#!/usr/bin/python3
"""Defines a function that check if object is exactly an instance"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance or inherited instance of a class

    Args:
        obj (any): object to be checked
        a_class (type): class type to be matched with object
    Returns:
        True if obj is an instance or inherited instance
        False otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False

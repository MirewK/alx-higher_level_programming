#!/usr/bin/python3
"""Defines a function that add an integer."""


def add_integer(a, b=98):
    """Adds two integers or floats.

    Floats are typecasted to ints before the operation

    Raises:
        TypeError: if the numbers are neither integer nor float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

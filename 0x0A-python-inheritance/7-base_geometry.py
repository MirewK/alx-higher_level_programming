#!/usr/bin/python3
"""Defines a BaseGeometry class"""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Raises Not implemented Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate parameter as an integer.

        Args:
            name (str): name of the parameter.
            value (int): parameter to validate
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

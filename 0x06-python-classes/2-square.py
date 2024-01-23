#!/usr/bin/python3

"""Defines a class Square."""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size=0):
        """
        Initializes a new Square instance with optional size.

        Args:
            size (int): the size of the square(defaults to 0).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

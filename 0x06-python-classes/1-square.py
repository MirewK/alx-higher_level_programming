#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square with a private size attribute."""
    def __init__(self, size):
        """
        Inittializes a new square instance with the given size.

        Args:
            size: the size of the squere(no type/value verification).
        """
        self.__size = size

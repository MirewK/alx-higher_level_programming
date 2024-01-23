#!/usr/bin/python3

"""Defines a class Square."""


class Square:
    """Represents a square wiht a private size attribute and area calculation."""

    def __init__(self, size=0):
        """
        Initializes a new Square instance with optional size.

        Args:
            size: the size of the square (defaults to 0).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates and returns the current square's area.

        Returns:
            The area of the square as an integer.
        """
        return self.__size * self.__size

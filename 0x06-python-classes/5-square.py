#!/usr/bin/python3

"""Defines a class Square"""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size=0):
        """
        Initializes a new square instance with optional size

        Args:
            size: the size of the square (defaults to 0).
        """
        self.size = size

    @property
    def size(self):
        """Retrives the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the current square's area"""
        return self.__size * self.__size

    def my_print(self):
        """Prints a visual representation of the square"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)

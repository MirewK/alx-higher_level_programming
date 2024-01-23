#!/usr/bin/python3

"""Defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new square instance

        Args:
            size: the size of the square (defaults to 0)
            position: the possition of the square (defaults to 0, 0)
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrives the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrives the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets the position of the square with validation."""
        if (not isinstance(value, tuple) or 
                len(value) != 2 or
                not all(isinstance(coord, int) for coord in value) or
                not all(coord >= 0 for coord in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns the area of a square."""
        return self.__size * self.__size

    def my_print(self):
        """prints a visual representation of the square."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

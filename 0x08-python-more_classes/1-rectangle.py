#!/usr/bin/python3
"""Defines a rectangle class."""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with optional width and height.

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """Retrives the rectangle's width."""
        return self._width

    @width.setter
    def width(self, value):
        """Sets the rectangle's width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Retrives the rectangle's height."""
        return self._height

    @height.setter
    def height(self, value):
        """Sets the rectangle's height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

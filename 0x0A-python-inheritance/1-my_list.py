#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """Return a sorted(ascending sort) list."""

    def print_sorted(self):
        """Print the sorted list."""
        print(sorted(self))

#!/usr/bin/python3
"""Defines the lookup function that list available attribute"""


def lookup(obj):
    """Return the list of objects attributes and methods"""
    return (dir(obj))

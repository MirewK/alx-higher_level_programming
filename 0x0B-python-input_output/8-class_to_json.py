#!/usr/bin/python3
"""Defines a function class to json"""


def class_to_json(obj):
    """Return the dictionary description with simple data structure"""
    return obj.__dict__

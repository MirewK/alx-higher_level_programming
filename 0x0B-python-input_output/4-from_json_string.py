#!/usr/bin/python3
"""Defines a function object to JSON string"""
import json


def from_json_string(my_str):
    """Retuns an object(python data structure)represented by JSON string"""
    return json.loads(my_str)

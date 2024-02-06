#!/usr/bin/python3
"""Defines a class student"""


class Student:
    """Represent a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new student

        Args:
            first_name (str): first name of the student
            last_name (str): last name of the student
            age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the student

        if attrs is a list of strings, only attribute names 
        contained in this list must be retrieved

        Args:
            attrs (list): attributes to represent (optional)
        """
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the student

        Args:
            json (dict): the key/value pairs to replace attributes
        """
        for k, v in json.items():
            setattr(self, k, v)

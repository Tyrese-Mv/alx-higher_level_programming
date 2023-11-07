#!/usr/bin/python3
"""Student"""


class Student:

    """Student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        """instance function


        Args:
            Attrs: none by default
        """
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for item in attrs:
            if hasattr(self, x):
                new_dict[item] = getattr(self, item)
        return new_dict

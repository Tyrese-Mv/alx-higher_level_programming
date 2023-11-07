#!/usr/bin/python3
"""Student"""


class Student:

    """Student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """attribute"""
        return self.__dict__

    def to_json(self, attrs=None):

    """instance function
    Args:
        attrs: none by default
    """
        if attrs == None:
            return self.__dict__
        return {key: getattr(self, key) for key in attrs if hasattr(self,key)}

#!/usr/bin/python3

"""Geometry class"""


class BaseGeometry:
    """create empty geometry class"""

    def area(self):
        """raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(self.value) != int:
            raise TypeError("{} must be an integer".format(self.name))
        elif self.value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))

#!/usr/bin/python3
"""Square"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """instantiate child class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        return self.__size * self.__size

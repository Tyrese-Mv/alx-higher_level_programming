#!/usr/bin/python3
"""Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """instantiate child class"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def __str__(self):
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        return self.__width * self.__height

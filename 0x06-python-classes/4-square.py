#!/usr/bin/python3
"""square class"""


class Square:
    """initialising the class attributes
    Args:
        size: initialise size.
    """
    def __init__(self, size=0):
        if int(size) >= 0:
            self.__size = size
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")
    """
    Getter
    Arg:
        self: self
    """
    def get_size(self):
        return self.__size
    """
    Setter
    Arg:
        self: self
    """
    def set_size(self, value):
        if int(value) >= 0:
            self.__size = value
        elif not isinstance(value, int):
            raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")
    """
    method that returns current square area
    Arg:
        self: the size of the instatiated square
    """
    def area(self):
        return self.__size*self.__size

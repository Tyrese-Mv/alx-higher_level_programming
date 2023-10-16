#!/usr/bin/python3
"""square class"""


class Square:
    """initialising the class attributes
    Args:
        size: initialise size.
    """
    def __init__(self, size=0):
        if int(size) >= 0:
            self.__size = int(size)
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")

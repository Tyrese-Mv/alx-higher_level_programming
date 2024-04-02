#!/usr/bin/python3
"""square class"""


class Square:
    """initialising the class attributes
    Args:
    size: initialise size.
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if int(value) >= 0:
            self.__size = value
        elif not isinstance(value, int):
            raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if int(value[0]) >= 0 and int(value[1]) >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
    def area(self):
        return self.__size*self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print("{}".format(" "*self.__position[0]), end="")
                print("#"*self.__size)

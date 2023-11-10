#!/usr/bin/python3
"""Rectangle class"""


class Rectangle(Base):
    """Rectangle inheriting from base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__ = id
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.width

    @setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width
    
    @property
    def height(self):
            return self.height
    
    @setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("width must be an integer")
        elif height <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        return self.x

    @setter
    def x(self, x):
        if x <= 0:
            raise ValueError("x must be >= 0")
        self.__x = x
    
    @property
    def y(self):
        return self.y

    @setter
    def y(self, y):
        if y <= 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        return self.__height * self.__width

    def display(self):
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(id(self), self.__x, self.__y, self.width, self.height)

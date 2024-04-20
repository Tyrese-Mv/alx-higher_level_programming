#!/usr/bin/python3
"""Rectangle Module"""

from models.base import Base

class Rectangle(Base):
    """Rectangle class"""
    
    def __init__(self, width, height, x=0, y=0, id=None):
        
        super().__init__(id)
        Rectangle.__validation(self, width=width, height=height, x=x, y=y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif int(value) >= 0:
            self.__width = value
        else:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif int(value) >= 0:
            self.__height = value
        else:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif int(value) >= 0:
            self.__x = value
        else:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif int(value) >= 0:
            self.__y = value
        else:
            raise ValueError("y must be >= 0")

    def __validation(self, **kwargs):
        """Validates the instance attributes
        Raises:
            TypeError: <name of the attribute> must be an integer
            ValueError: <name of the attribute> must be > 0
            ValueError: <name of the attribute> must be >= 0
        """

        for key, val in kwargs.items():
            if not isinstance(val, int):
                raise TypeError("{} must be an integer".format(key))
            if key == "width" or key == "height":
                if int(val) <= 0:
                    raise ValueError("{} must be > 0".format(key))
            if key == "x" or key == "y":
                if int(val) < 0:
                    raise ValueError("{} must be >= 0".format(key))
    
    def area(self):
        return self.width * self.height
    
    def display(self):
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print("{}".format(" " * self.x if self.x > 0 else ""), end="")
            print("#" * self.width)
    
    def __str__(self):
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__, self.id, self.x, self.y, self.width, self.height)
       
    def update(self, *args):
        for index in range(len(args)):
            match index:
                case 0:
                    self.id = args[index]
                case 1:
                    self.width = args[index]
                case 2:
                    self.height = args[index]
                case 3:
                    self.x = args[index]
                case 4:
                    self.y = args[index]
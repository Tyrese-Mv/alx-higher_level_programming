#!/usr/bin/python3
"""Square Module"""

from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        Rectangle._validation(self, width=value, height=value)
        self.width = value

    def __str__(self):
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id,
                                             self.x,
                                             self.y,
                                             self.width)

    def update(self, *args, **kwargs):
        if (args and len(args) > 0):
            for index in range(len(args)):
                match index:
                    case 0:
                        self.id = args[index]
                    case 1:
                        self.size = args[index]
                    case 2:
                        self.x = args[index]
                    case 3:
                        self.y = args[index]
        else:
            for key, val in kwargs.items():
                match key:
                    case "id":
                        self.id = val
                    case "size":
                        self.size = val
                    case "x":
                        self.x = val
                    case "y":
                        self.y = val

    def to_dictionary(self):
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

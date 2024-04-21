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
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__, self.id, self.x, self.y, self.width)

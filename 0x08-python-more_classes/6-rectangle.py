#!/usr/bin/python3
"""Empty Class"""


class Rectangle:
    """empty class"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value

    def area(self):
        """calculates and returns area"""
        return self.height * self.width

    def perimeter(self):
        """Calculates and returns perimeter"""
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """String representation of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.height):
            rectangle_str += "#" * self.width + "\n"
        return rectangle_str.strip()

    def __repr__(self):
        """Representation of the rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """deletes instance"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

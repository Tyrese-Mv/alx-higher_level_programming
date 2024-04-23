#!/usr/bin/python3

"""Square Module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class

    Args:
        Rectangle (class): inherits rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter

        Returns:
            int: width of the rectangle
        """
        return self.width

    @size.setter
    def size(self, value):
        """updates width value

        Args:
            value (int): value used to update width

        Raises:
            TypeError: width must be an integer
            ValueError: width must be > 0
        """
        Rectangle._validation(self, width=value, height=value)
        self.width = value

    def __str__(self):
        """string representation of the square class

        Returns:
            _type_: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id,
                                             self.x,
                                             self.y,
                                             self.width)

    def update(self, *args, **kwargs):
        if args:
            for index, value in enumerate(args):
                if index == 0:
                    self.id = value
                elif index == 1:
                    self.size = value
                elif index == 2:
                    self.x = value
                elif index == 3:
                    self.y = value
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """dictionary representation of the instance
        Returns:
            _type_: dictionary
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

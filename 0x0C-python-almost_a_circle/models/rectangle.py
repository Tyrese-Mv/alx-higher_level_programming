#!/usr/bin/python3

"""Rectangle Module"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """rectangle constructor

        Args:
            width (int): _description_
            height (int): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (int, optional): _description_. Defaults to None.
        """
        super().__init__(id)
        Rectangle._validation(self, width=width, height=height, x=x, y=y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """width getter

        Returns:
            int: width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """updates width value

        Args:
            value (int): value used to update width

        Raises:
            TypeError: width must be an integer
            ValueError: width must be > 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif int(value) >= 0:
            self.__width = value
        else:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """height getter

        Returns:
            int: height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """updates height value

        Args:
            value (int): value used to update height

        Raises:
            TypeError: height must be an integer
            ValueError: height must be > 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif int(value) >= 0:
            self.__height = value
        else:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """x getter

        Returns:
            int: x of the rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """updates x value

        Args:
            value (int): value used to update x

        Raises:
            TypeError: x must be an integer
            ValueError: x must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif int(value) >= 0:
            self.__x = value
        else:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """y getter

        Returns:
            int: y of the rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """updates y value

        Args:
            value (int): value used to update y

        Raises:
            TypeError: y must be an integer
            ValueError: y must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif int(value) >= 0:
            self.__y = value
        else:
            raise ValueError("y must be >= 0")

    def _validation(self, **kwargs):
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
        """calculates area of the rectangle

        Returns:
            int: product of widht and height
        """
        return self.width * self.height

    def display(self):
        """draws the rectangle
        """
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print("{}".format(" " * self.x if self.x > 0 else ""), end="")
            print("#" * self.width)

    def __str__(self):
        """string representation of the rectangle class

        Returns:
            _type_: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id,
                                                self.x,
                                                self.y,
                                                self.width,
                                                self.height)

    def update(self, *args, **kwargs):
        """Updates the instance with values passed in
        """
        if len(args) > 0:
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
        else:
            for key, val in kwargs.items():
                match key:
                    case "id":
                        self.id = val
                    case "width":
                        self.width = val
                    case "height":
                        self.height = val
                    case "x":
                        self.x = val
                    case "y":
                        self.y = val

    def to_dictionary(self):
        """dictionary representation of the instance

        Returns:
            _type_: dictionary
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

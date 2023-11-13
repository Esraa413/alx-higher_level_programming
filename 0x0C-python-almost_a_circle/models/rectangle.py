#!/usr/bin/python3
"""rectangle class."""
from models.base import Base


class Rectangle(Base):
    """rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle.

        Args:
            width (int): width a new Rectangle.
            height (int): height a new Rectangle.
            x (int): x coordinate anew Rectangle.
            y (int): y coordinate a new Rectangle.
            id (int): id entity a new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width a Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height a Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x coordinate a Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y coordinate a Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return area Rectangle."""
        return self.width * self.height

    def display(self):
        """Printed Rectangle to  using `#` char."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """Update Rectangle.

        Args:
            *args (ints): New values attribute.
                - 1 argument represents id
                - 2 argument represents width
                - 3 argument represent height
                - 4 argument represents x
                - 5 argument represents y
            **kwargs (dict): New key/value
        """
        if args and len(args) != 0:
            ar = 0
            for arg in args:
                if ar == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                if ar == 1:
                    self.width = arg
                if ar == 2:
                    self.height = arg
                if ar == 3:
                    self.x = arg
                if ar == 4:
                    self.y = arg
                ar += 1

        if kwargs and len(kwargs) != 0:
            for w, h in kwargs.items():
                if w == "id":
                    if h is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = h
                if w == "width":
                    self.width = h
                if w == "height":
                    self.height = h
                if w == "x":
                    self.x = h
                if w == "y":
                    self.y = h

    def to_dictionary(self):
        """Return dictionary representation Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

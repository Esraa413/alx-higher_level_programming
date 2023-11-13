#!/usr/bin/python3
"""Class Square that inherits from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent the square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a square.

        Args:
            size (int): size of Square.
            x (int): x coordinate Square.
            y (int): y coordinate Square.
            id (int): identity Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """The size of Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return print() and str() representation of Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """Update Square.

        Args:
            *args (ints): New values attribute.
                - 1 argument represents id.
                - 2 argument represents size.
                - 3 argument represents x.
                - 4 argument represents y.
            **kwargs (dict): New key/value pairs.
        """
        if args and len(args) != 0:
            ar = 0
            for arg in args:
                if ar == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                if ar == 1:
                    self.size = arg
                if ar == 2:
                    self.x = arg
                if ar == 3:
                    self.y = arg
                ar += 1

        if kwargs and len(kwargs) != 0:
            for w, h in kwargs.items():
                if w == "id":
                    if h is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = h
                if w == "size":
                    self.size = h
                if w == "x":
                    self.x = h
                if w == "y":
                    self.y = h

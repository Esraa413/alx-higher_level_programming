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

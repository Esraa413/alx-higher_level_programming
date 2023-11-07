#!/usr/bin/python3
"""function Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a new square."""

    def __init__(self, size):
        """Initialize square.

        Args:
            size (int): of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

#!/usr/bin/python3

"""class Square."""


class Square:
    """class defines a square"""

    def __init__(self, size=0):
        """Initialize with size.
        Args:
            size (int):  size of new square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

#!/usr/bin/python3

"""class Square."""


class Square:
    """class defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize with size.
        Args:
            size (int): size of new square.
            position (int, int): new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """current size of square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """current position of square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(number, int) for number in value) or
                not all(number >= 0 for number in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return  area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square."""
        if self.__size == 0:
            print("")
            return

        [print("") for x in range(0, self.__position[1])]
        for x in range(0, self.__size):
            [print(" ", end="") for y in range(0, self.__position[0])]
            [print("#", end="") for i in range(0, self.__size)]
            print("")

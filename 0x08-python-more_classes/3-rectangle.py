#!/usr/bin/python3

"""empty Rectangle class using the pass keyword"""


class Rectangle:
    """Represent defines a rectangle.

    Args:
        width (int): the width
        height (int): the height
    """

    def __init__(self, width=0, height=0):
        """optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """to retrieve it"""
        return self.__width

    @width.setter
    def width(self, value):
        """width must be an integer, otherwise raise a TypeError"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """instance attribute: height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ must be an integer, otherwise raise a TypeError"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public instance method"""
        return self.__width * self.__height

    def perimeter(self):
        """Public instance method"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """printable representation of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for x in range(self.__height):
            [rect.append('#') for y in range(self.__width)]
            if x != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

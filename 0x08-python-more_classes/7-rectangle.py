#!/usr/bin/python3

"""empty Rectangle class using the pass keyword"""


class Rectangle:
    """Represent defines a rectang"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """optional width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        else:
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
        else:
            self.__width = value

    def area(self):
        """Public instance method"""
        return self.__width * self.__height

    def perimeter(self):
        """Public instance method"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """printable representation of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return ((str(self.print_symbol) * self.__width + "\n") * self.__height)[:-1]

    def __repr__(self):
        """return a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """instance of Rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

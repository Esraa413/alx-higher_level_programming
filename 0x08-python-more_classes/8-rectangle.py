#!/usr/bin/python3

"""empty Rectangle class using the pass keyword"""


class Rectangle:
    """Represent defines a rectangle.

    Args:
        width (int): the width
        height (int): the height
    """
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
        elif value < 0:
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
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Public instance method"""

        return self.width * self.height

    def perimeter(self):
        """Public instance method"""

        if self.width == 0 or self.height == 0:
            return 0

        return 2 * (self.width + self.height)

    def __str__(self):
        """printable representation of the Rectangle"""

        if self.width == 0 or self.height == 0:
            return ""

        rectangle = ""
        for x in range(self.height):
            for y in range(self.width):
                rectangle += str(self.print_symbol)
            if x != self.height - 1:
                rectangle += "\n"

        return rectangle

    def __repr__(self):
        """return a string representation of the rectangle"""

        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """instance of Rectangle is deleted"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """from BaseGeometry(7-base_geometry.py).(task based on 8-rectangle.py)."""

     def __init__(self, width, height):
         """Instantiation with width and height.

         Args:
            width: of the new Rectangle.
            height: of the new Rectangle.
         """
         super().integer_validator("width", width)
         self.__width = width
         super().integer_validator("height", height)
         self.__height = height

    def area(self):
        """Return the area."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str()."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string

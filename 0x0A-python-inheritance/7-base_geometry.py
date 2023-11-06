#!/usr/bin/python3
"""class BaseGeometry."""


class BaseGeometry:
    """class BaseGeometry (based on 6-base_geometry.py)."""

    def area(self):
        """that raises an Exception with the message,
        area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ that validates value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

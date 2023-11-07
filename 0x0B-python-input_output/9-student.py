#!/usr/bin/python3
"""class Student that defines a student"""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize  Student.

        Args:
            first_name (str): student first name
            last_name (str): student last name
            age (int): The age student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dictionary representation."""
        return self.__dict__

#!/usr/bin/python3
"""function class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize Student.

        Args:
            first_name (str): student first name 
            last_name (str): student last name
            age (int): The age student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def to_json(self, attrs=None):
        """Get a dictionary representation.


        Args:
            attrs (list): attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    


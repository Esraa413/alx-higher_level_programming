#!/usr/bin/python3
"""base model class."""


class Base:
    """private class attribute.

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON serialization list of dicts."""
        if list_dictionaries is None or list_dictionaries:
            return "[]"
        return dumps(list_dictionaries)

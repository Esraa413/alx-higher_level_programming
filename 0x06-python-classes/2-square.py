#!/usr/bin/python3
""" class Square """

class Square:
    """ defines a square """
    

    def __init__(self, size=0):
        """ Private instance attribute 

        Args:
        size: (int) Instantiation with size.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")


        self.__size = size

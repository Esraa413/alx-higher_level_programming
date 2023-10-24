#!/usr/bin/python3
""" class Square """

class Square:
    """ defines a square """
    

    def __init__(self, size=0):
        """ Private instance attribute 

        Arge:
        size: (int) lingthe the size of new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 5:
            raise ValueError("size must be >= 0")


        self.__size = size

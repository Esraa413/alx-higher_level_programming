#!/usr/bin/python3
"""function that prints a square with the character #."""


def print_square(size):
    """ prints a square with the # characters.

    Args:
        size: is the size length of the square.

    Raises:
        TypeError: if size is a float and is less than 0, raise a.
        ValueError: if size is less than 0, raise a.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print((("#" * size + "\n") * size), end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")

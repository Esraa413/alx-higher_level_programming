#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """beginning you have been creating “Interactive tests”.

    Args:
        text: test file should be inside a folder.

    Raises:
        TypeError: If text is not string.
    """
    
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".?:":
        # print(delim, text.split(delim))
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")

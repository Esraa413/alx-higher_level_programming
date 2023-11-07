#!/usr/bin/python3
"""function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """If the file doesn’t exist, it should be created.

    Args:
        filename (str): The name  file to append to.
        text (str): The string file to append to.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

#!/usr/bin/python3
"""function file-writing function."""


def write_file(filename="", text=""):
    """Write a string to a UTF8.

    Args:
        filename (str): write the file name
        text (str): write the text file 
    Returns:
        number characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

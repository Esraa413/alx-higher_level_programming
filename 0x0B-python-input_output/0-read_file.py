#!/usr/bin/python3
"""function text file-reading function."""


def read_file(filename=""):
    """Print the contents of a UTF8 text fil."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

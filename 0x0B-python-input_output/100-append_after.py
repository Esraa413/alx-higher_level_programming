#!/usr/bin/python3
"""functiona text file insertion ."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing .

    Args:
        filename (str): name  file.
        search_string (str): string to search for within the file.
        new_string (str): string insert.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)

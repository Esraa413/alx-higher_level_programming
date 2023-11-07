#!/usr/bin/python3
"""function that writes an Object to a text file."""
import json


def load_from_json_file(filename):
    """writes an Object to a text file, using a JSON representation."""
    with open(filename) as f:
        return json.load(f)

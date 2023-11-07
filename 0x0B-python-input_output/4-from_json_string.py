#!/usr/bin/python3
"""function that returns an object."""
import json


def from_json_string(my_str):
    """ returns an object (Python data structure) represented."""
    return json.loads(my_str)

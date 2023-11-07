#!/usr/bin/python3
"""function that returns the JSON representation."""
import json


def to_json_string(my_obj):
    """JSON representation of an object (string)."""
    return json.dumps(my_obj)

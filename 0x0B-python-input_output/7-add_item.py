#!/usr/bin/python3
"""script that adds all arguments to a Python list."""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file =  __import__('6-load_from_json_file').load_from_json_file

arglist = list(sys.argv[1:])

    try:
        add_data = load_from_json_file("add_item.json")
    except FileNotFoundError:
        add_data = []

    add_data.extend(arglist)
    save_to_json_file(add_data, "add_item.json")

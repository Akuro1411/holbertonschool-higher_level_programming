#!/usr/bin/python3
"""
imports json module
"""
import json


def save_to_json_file(my_obj, filename):
    """
    opens and saves the object in file
    """
    with open(filename, "w") as new_file:
        text = json.dumps(my_obj)
        new_file.write(text)
    return new_file

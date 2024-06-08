#!/usr/bin/python3
"""
json module
"""
import json


def load_from_json_file(filename):
    """
    makes python object from json file
    """
    with open(filename, "r") as new_file:
        a = new_file.read()
    b = json.loads(a)
    return b

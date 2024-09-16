#!/usr/bin/python3
"""
json module
"""
import json


def load_from_json_file(filename):
    """
    makes python object from json file
    """
    with open(filename, encoding="UTF-8") as file:
        obj = json.load(fp=file)
    return obj

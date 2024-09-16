#!/usr/bin/python3
"""
imports json module
"""
import json


def save_to_json_file(my_obj, filename):
    """
    opens and saves the object in file
    """
    with open(filename, encoding="UTF-8", mode="w") as file:
        json.dump(my_obj, fp=file)

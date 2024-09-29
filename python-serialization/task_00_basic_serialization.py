#!/usr/bin/env python3
"""
pickle module for serialize and inverse operation
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    serialize data and write it in file
    """
    with open(filename, encoding="UTF-8", mode="w") as file:
        json.dump(data, fp=file)


def load_and_deserialize(filename):
    """
    deserialize data and read it
    """
    with open(filename, encoding="UTF-8") as file:
        data = json.load(file)
    return data

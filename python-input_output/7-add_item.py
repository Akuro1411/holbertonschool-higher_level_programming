#!/usr/bin/python3
"""
json, sys and os were imported for this code
"""
import json
from sys import argv
from os.path import isfile


def save_to_json_file(my_obj, filename):
    """
    opens and saves the object in file
    """
    with open(filename, "w") as new_file:
        text = json.dumps(my_obj)
        new_file.write(text)
    return new_file


def load_from_json_file(filename):
    """
    makes python object from json file
    """
    with open(filename, "r") as new_file:
        a = new_file.read()
    b = json.loads(a)
    return b


file = "add_item.json"
if not isfile(file):
    arr = []
else:
    arr = load_from_json_file(file)

n = len(argv)
for i in range(1, n):
    arr.append(argv[i])

save_to_json_file(arr, file)

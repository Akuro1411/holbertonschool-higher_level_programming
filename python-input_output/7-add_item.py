#!/usr/bin/python3
"""
The modules are used for convert the object and put it in json file
"""
import json
from sys import argv
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file = "add_item.json"

if not os.path.exists("./add_item.json"):
    storage = []
    save_to_json_file(storage, file)

storage = load_from_json_file(file)
for i in range(len(argv)):
    if i == 0:
        continue
    storage.append(argv[i])

save_to_json_file(storage, file)

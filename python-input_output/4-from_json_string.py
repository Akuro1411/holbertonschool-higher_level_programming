#!/usr/bin/python3
"""
json module for encoding and decoding
"""
import json


def from_json_string(my_str):
    """
    returns json strings
    """
    return json.loads(my_str)

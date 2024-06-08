#!/usr/bin/python3
"""
Json module for json object
"""
import json


def to_json_string(my_obj):
    """
    Returns json represantation of object
    """
    return json.dumps(my_obj)

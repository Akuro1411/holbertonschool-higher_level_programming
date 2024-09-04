#!/usr/bin/python3
"""
Defines the function for list of attributes
"""


def lookup(obj):
    """
    :param obj:
    :return: Returns the list of available attributes
    """
    arr = dir(obj)
    return arr

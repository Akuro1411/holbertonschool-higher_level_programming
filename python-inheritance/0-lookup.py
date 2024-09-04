#!/usr/bin/python3
def lookup(obj):
    """
    :param obj:
    :return: Returns the list of available attributes
    """
    arr = dir(obj)
    return arr

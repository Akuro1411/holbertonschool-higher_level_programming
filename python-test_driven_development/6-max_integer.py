#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(arr=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(arr) == 0:
        return None
    result = arr[0]
    i = 1
    while i < len(arr):
        if arr[i] > result:
            result = arr[i]
        i += 1
    return result

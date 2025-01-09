#!/usr/bin/python3
"""No module is imported for testing"""


def add_integer(a, b=98):
    """Function adds 2 number and finds their final value"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return round(a) + round(b)

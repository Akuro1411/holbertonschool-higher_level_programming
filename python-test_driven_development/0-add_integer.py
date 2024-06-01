#!/usr/bin/python3
"""
No module is here
"""
def add_integer(a, b=98):
    """
    Adding 2 integer or float number
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return a + b

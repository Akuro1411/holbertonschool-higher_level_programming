#!/usr/bin/python3
"""No module is imported"""


def say_my_name(first_name, last_name=""):
    """Function prints the first_name and last_name"""
    if type(first_name) not in [str]:
        raise TypeError("first_name must be a string")

    if type(last_name) not in [str]:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")

#!/usr/bin/python3
"""
Module is documanted
"""
def say_my_name(first_name, last_name=""):
    """
    Fucntion prints first and last names.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("first_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

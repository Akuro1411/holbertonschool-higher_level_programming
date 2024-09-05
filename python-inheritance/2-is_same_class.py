#!/usr/bin/python3
"""
No module is imported.Function is for checking instance
"""


def is_same_class(obj, a_class):
    """
    :param obj: The object for checking
    :param a_class: The class for checking
    :return: Returns True if object belongs to class: otherwise False
    """
    return type(obj) is a_class

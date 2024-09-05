#!/usr/bin/python3
"""
No module is imported.Function is for checking instance
"""


def inherits_from(obj, a_class):
    """
    :param obj: The object for checking
    :param a_class: The class for checking
    :return: Returns True if object belongs to class: otherwise False
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False

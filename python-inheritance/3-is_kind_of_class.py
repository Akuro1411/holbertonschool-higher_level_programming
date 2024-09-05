#!/usr/bin/python3
"""
No module is imported.Function is for checking instance class or parent class
"""


def is_kind_of_class(obj, a_class):
    """
    :param obj: The object for checking
    :param a_class: The class for checking
    :return: Returns True if object belongs to class: otherwise False
    """
    return isinstance(obj, a_class)

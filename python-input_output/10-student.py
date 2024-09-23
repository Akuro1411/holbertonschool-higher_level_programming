#!/usr/bin/python3
"""
no module
"""


class Student:
    """
    Makes student class with name and age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        changes to dict format
        """
        new_obj = self.__dict__
        if attrs is not None:
            new_dict = {i: new_obj[i] for i in attrs if i in new_obj}
            return new_dict
        return new_obj

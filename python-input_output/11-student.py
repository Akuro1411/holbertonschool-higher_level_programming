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
        student = Student(self.first_name, self.last_name, self.age).__dict__
        if attrs is not None:
            new_dict = {}
            for i in attrs:
                if i in student:
                    new_dict[i] = student[i]
            return new_dict
        return student

    def reload_from_json(self, json):
        """
        changes public attributes
        """
        for key, value in json.items():
            setattr(self, key, value)

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

    def to_json(self):
        """
        changes to dict format
        """
        student = Student(self.first_name, self.last_name, self.age)
        return student.__dict__

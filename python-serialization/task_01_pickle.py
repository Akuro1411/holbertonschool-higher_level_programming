#!/usr/bin/env python3
"""
pickle module is imported
"""
import pickle


class CustomObject:
    """The CustomObject class"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        :return: Displays the attributes of class 
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        :param filename: 
        :return: Serializes the data to file
        """
        try:
            with open(filename, mode="wb") as file:
                pickle.dump(self, file)
        except IOError:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        :param filename: 
        :return: Deserializes the data from file 
        """
        try:
            with open(filename, mode="rb") as file:
                data = pickle.load(file)
            return data
        except Exception:
            return None

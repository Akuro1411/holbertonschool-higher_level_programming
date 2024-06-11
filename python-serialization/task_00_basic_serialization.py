#!/usr/bin/python3
"""
pickle module for serialize and inverse operation
"""
import pickle


def serialize_and_save_to_file(data, filename):
    """
    serialize data and write it in file
    """
    with open(filename, "wb") as file:
        pickle.dump(data, file)


def load_and_deserialize(filename):
    """
    deserialize data and read it
    """
    with open(filename, "rb") as file:
        data = file.read()
        pickle.loads(data)

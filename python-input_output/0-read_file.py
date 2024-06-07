#!/usr/bin/python3
"""
No module needed
"""
def read_file(filename=""):
    """
    opens the file and reads
    """
    with open(filename) as new_file:
        file = new_file.read()
    return file

#!/usr/bin/python3
"""
No module needed
"""


def read_file(filename=""):
    """
    opens the file and reads
    """
    with open(filename, encoding="UTF-8") as file:
        print(file.read())

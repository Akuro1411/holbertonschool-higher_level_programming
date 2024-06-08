#!/usr/bin/python3
"""
No module needed
"""


def write_file(filename="", text=""):
    """
    opens the file and writes
    """
    with open(filename, "w") as new_file:
        file = new_file.write(text)
    i = len(text)
    return i

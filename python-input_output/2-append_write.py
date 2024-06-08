#!/usr/bin/python3
"""
No module needed
"""

def append_write(filename="", text=""):
    """
    opens the file and appends the text
    """
    with open(filename, "a") as new_file:
        file = new_file.write(text)
    i = len(text)
    return i

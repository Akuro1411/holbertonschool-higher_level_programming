#!/usr/bin/python3
"""
No module needed
"""


def write_file(filename="", text=""):
    """
    opens the file and writes
    """
    with open(filename, encoding="UTF-8", mode="w") as file:
        file.write(text)
    return len(text)

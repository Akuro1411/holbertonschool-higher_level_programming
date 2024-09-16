#!/usr/bin/python3
"""
No module needed
"""


def append_write(filename="", text=""):
    """
    opens the file and appends the text
    """
    def append_write(filename="", text=""):
    with open(filename, encoding="UTF-8", mode="a") as file:
        file.write(text)
    return len(text)

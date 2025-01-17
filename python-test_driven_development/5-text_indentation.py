#!/usr/bin/python3
"""No module is imported"""

def text_indentation(text):
    """Function prints text line byline"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] in ["?", ".", ":"]:
            print(text[i], end="")
            print('\n')
            if i + 1 < len(text) and text[i + 1] == " ":
                i += 2
                continue
        else:
            print(text[i], end="")
        i += 1

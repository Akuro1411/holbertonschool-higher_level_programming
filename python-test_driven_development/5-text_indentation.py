#!/usr/bin/python3
"""
Module is documented
"""
def text_indentation(text):
    """
    Function is documented
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if (text[i-1] == "." or text[i-1] == "?" or text[i-1] == ":") and text[i] == " ":
            print("", end="")
        else:
            print(text[i], end="")
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print("\n")

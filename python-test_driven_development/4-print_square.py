#!/usr/bin/python3
"""No module is imported"""


def print_square(size):
    """Function prints the square's edges with given size"""
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    elif type(size) is not int:
        raise TypeError("size must be an integer")

    elif size < 0:
        raise ValueError("size must be >= 0")

    square = ""
    for edge in range(size):
        square += '#' * size
        if edge < size - 1:
            square += '\n'
    print(square)

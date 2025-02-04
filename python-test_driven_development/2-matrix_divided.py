#!/usr/bin/python3
"""No module is imported"""


def matrix_divided(matrix, div):
    """Function should divide matrix with given division number"""
    m = matrix
    type_list = [n for r in m for n in r if type(n) not in [float, int]]
    size_list = [len(row) for row in matrix if len(row) != len(matrix[0])]

    if type_list:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    elif size_list:
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    def func(number): return round(number / div, 2)

    new_mat = list(map(lambda row:  list(map(func, row)), matrix))
    return new_mat

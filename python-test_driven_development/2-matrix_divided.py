#!/usr/bin/python3
def matrix_divided(matrix, div):
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    a = len(matrix[0])
    for i in matrix:
        if len(i) != a:
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    new_matrix = []
    for i in matrix:
        new_row = []
        for j in i:
            j = round(j / div, 2)
            new_row.append(j)
        new_matrix.append(new_row)
    return new_matrix


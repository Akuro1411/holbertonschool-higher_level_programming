#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = []
    for i in matrix:
        new_row = []
        for j in i:
            new_row.append(j*j)
        new_mat.append(new_row)
    return new_mat

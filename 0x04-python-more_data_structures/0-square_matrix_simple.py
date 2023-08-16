#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for row in new_matrix:
        for element in row:
            row[element] = map(lambda x: x**2)
    return new_matrix

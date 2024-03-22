#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [row[:] for row in matrix]
    for row in range(len(new_matrix)):
        for element in range(len(new_matrix[row])):
            new_matrix[row][element] = new_matrix[row][element] ** 2
    return new_matrix

#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nm = matrix[:]
    for row in range(len(matrix)):
        for column in range(len(matrix)):
            nm[row][column] = matrix[row][column] * matrix[row][column]
    return nm

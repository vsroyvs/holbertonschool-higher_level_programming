#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nm = matrix.copy()
    for i in range(len(matrix)):
        nm[i] = list(map(lambda x: x**2, matrix[i]))
    return nm

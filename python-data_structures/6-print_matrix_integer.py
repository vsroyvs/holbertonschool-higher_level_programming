#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for fila in matrix:
        for val in fila:
            print("{:d}".format(val), end=" ")
        print()

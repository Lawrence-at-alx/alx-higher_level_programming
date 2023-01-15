#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []

    if len(matrix) > 0:
        for elems in matrix[:]:
            new_matrix.append([x for x**2 in elems])
    return new_matrix

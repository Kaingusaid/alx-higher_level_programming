#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for spot in range(0, len(matrix)):
        square_matrix.append(list(map(lambda x: x * x, matrix[spot])))
    return square_matrix

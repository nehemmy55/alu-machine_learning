#!/usr/bin/env python3

"""" Transposing a matrix
"""""

def matrix_transpose(matrix: list):

    new_matrix = []
    for x in range(len(matrix[0])):
        piece = []
        for i in matrix:
            piece.append(i[x])
        new_matrix.append(piece)
    return new_matrix

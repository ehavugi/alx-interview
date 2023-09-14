#!/usr/bin/python3
"""
Rotate a matrix in place.
"""


def rotate_2d_matrix(matrix):
    """Rotate a mtrix in place.
        1. exchange mirror items along diagonal?
        2. mirror items around center vertical line
        3. check for  a given case
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i] = matrix[i][::-1]

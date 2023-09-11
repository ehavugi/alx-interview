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
        for j in range(n):
            if i <= j:
                x = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = x
    for i in range(n):
        notdone = True
        for j in range(n):
            if j <= n//2:
                x = matrix[i][j]
                matrix[i][j] = matrix[i][n-j-1]
                matrix[i][n-j-1] = x

    pass

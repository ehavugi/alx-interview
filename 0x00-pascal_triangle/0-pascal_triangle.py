#!/usr/bin/python3
"""
0-pascal_triangle.py
"""


def pascal_triangle(n, pascal=[[]]):
    """
        return empty list if n<=0
        n is assumed to always an integer
    """

    if n == 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    pascal = [[1]]
    for i in range(n-1):
        nthLine = [1, ]
        for j in range(len(pascal[i])-1):
            nthLine.append(pascal[i][j]+pascal[i][j+1])
        nthLine.append(1)
        pascal.append(nthLine)

    return pascal

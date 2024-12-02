#!/usr/bin/python3
"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise.

 - Prototype: def rotate_2d_matrix(matrix):
 - Do not return anything. The matrix must be edited in-place.
 - You can assume the matrix will have 2 dimensions and will not be
   empty.
"""


def rotate_2d_matrix(matrix):
    """Rotates a n*n matrix 90 deg clockwise in-place"""
    n = len(matrix)

    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # reverse each row
    for row in matrix:
        row.reverse()

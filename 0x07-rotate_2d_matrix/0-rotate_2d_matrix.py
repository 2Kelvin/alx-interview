#!/usr/bin/python3
"""Rotating a 2D matrix"""


def rotate_2d_matrix(matrix):
    """Rotating a matrix"""
    matrix.reverse()
    for x in range(len(matrix)):
        for y in range(x):
            matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

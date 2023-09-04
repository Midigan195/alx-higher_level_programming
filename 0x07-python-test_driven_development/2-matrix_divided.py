#!/usr/bin/python3
"""
This module includes a function that divides a matrix

The module has a function that divides items of a matrix
"""


def matrix_divided(matrix, div):
    """
    matrix_divided divides all items in the matrix by div
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if (
        not isinstance(matrix, list)
        or not all(isinstance(i, list) for i in matrix)
        or not all(isinstance(i, (int, float)) for a in matrix for i in a)
    ):
        raise TypeError(msg)

    if not all(len(i) == len(matrix[0]) for i in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("Division by zero")

    new_matrix = []
    for sub in matrix:
        new_matrix.append(list(map(lambda x: round(x / div, 2), sub)))

    return new_matrix

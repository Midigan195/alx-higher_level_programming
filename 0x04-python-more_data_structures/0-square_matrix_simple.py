#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqaured_numbers = []
    for x in matrix:
        sqaured_numbers.append(list(map(lambda x: x ** 2, x)))
    return sqaured_numbers

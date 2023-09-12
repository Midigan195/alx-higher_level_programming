#!/usr/bin/python3
"""
This module defines a function that creates a triangle.

This module contains one function that creates a traingle.
This trinagle is returned as a list of list.
"""


def pascal_triangle(n):
    """
    Generate a triangle of sepcified height.

    Args:
        n (int): Height of triangle.
    Returns:
        A list of list that represents the triangle.
    """
    triangle = []
    if n <= 0:
        return triangle
    for i in range(0, n):
        row = []
        if i != 0:
            prev = triangle[i - 1]
        for j in range(0, i+1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(prev[j-1] + prev[j])
        triangle.append(row)
    return triangle

#!/usr/bin/python3
"""Defines a Pascal's Triangle function"""


def pascal_triangle(n):
    """
    Represent Pascal's Triangle of size n

    Returns a list of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        tria = triangle[-1]
        temp = [1]
        for i in range(len(tria) - 1):
            temp.append(tria[i] + tria[i + 1])
        temp.append(1)
        triangle.append(temp)
    return triangle

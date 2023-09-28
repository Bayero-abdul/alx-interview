#!/usr/bin/python3
"""
contains a function pascal_triangle(n) that
returns a list of lists of integers
representing the Pascal’s triangle of n:
"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n"""

    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        if i == 0:
            triangle.append([1])
        elif i == 1:
            triangle.append([1, 1])
        else:
            row = []
            row.append(1)
            last_row = triangle[i - 1]
            for i in range(len(last_row) - 1):
                row.append(last_row[i] + last_row[i + 1])
            row.append(1)
            triangle.append(row)

    return triangle

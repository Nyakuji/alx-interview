#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal's triangle of n
    """

    if n <= 0:
        return []

    # Initialize the Pascal's triangle as a list of lists
    triangle = []

    for i in range(n):
        row = [1]
        if triangle:
            prev_row = triangle[-1]
            for j in range(1, len(prev_row)):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)
        triangle.append(row)

    return triangle

#!/usr/bin/python3
"""
module
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the n-th row.
    
    Args:
        n (int): The number of rows of Pascal's Triangle to generate.
    
    Returns:
        list of list of int: A list of lists where each sublist represents a row in Pascal's Triangle.
    """
    if n < 0:
        return [[]]
    if n == 0:
        return 1
    basecase = [[1]]
    for i in range(1, n + 1):
        row = [1]
        for j in range(1, i):
            row.append(basecase[i - 1][j - 1] + basecase[i - 1][j])
        row.append(1)
        basecase.append(row)
    return basecase

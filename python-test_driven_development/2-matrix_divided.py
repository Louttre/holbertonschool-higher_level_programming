#!/usr/bin/python3
"""
This module provides functions for dividing matrices.
"""


def MustBeAMatrix():
    """
    Raises a TypeError with a specific message

    Raises:
        TypeError: Always raised with the message
        "matrix must be a matrix (list of lists) of integers/floats".
    """


    raise TypeError("matrix must be a matrix (list of lists) "
                    "of integers/floats")

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The divisor.

    Returns:
        list of lists: The new matrix with elements divided by the divisor.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
                   or if div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
        TypeError: If each row of the matrix does not have the same size.
    """

    if not isinstance(matrix, list):
        MustBeAMatrix()
    for row in matrix:
        if not isinstance(row, list):
            MustBeAMatrix()
    for row in matrix:
        for num in row:
            if not isinstance(num, (int, float)):
                MustBeAMatrix()
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix

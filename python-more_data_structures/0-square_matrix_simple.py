#!/usr/bin/python3
def square(a):
    return a * a


def square_matrix_simple(matrix=[]):
    new_matrix = [list(map(square, row)) for row in matrix]
    return list(new_matrix)

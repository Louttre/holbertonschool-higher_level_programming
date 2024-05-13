#!/usr/bin/python3
def square(a=0):
    return a * a
def square_matrix_simple(matrix=[]):
    new_matrix = map(square, matrix)
    return new_matrix

#!/usr/bin/python3
"""Divides a matrix"""


def matrix_divided(matrix, div):
    """matrix division
    Arguments:
        arg1 (matrix): the matrix to divide
        arg2 (div): number to divide by
    """
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integer/\
        floats")
    length = 0
    new_matrix = []
    overf = "Each row of the matrix must have the same size"
    form = "matrix must be a matrix (list of lists) of integer/floats"
    for y, row in enumerate(matrix):
        new_matrix.append([])
        if y > 0:
            if len(row) != length:
                raise TypeError(overf)
        for x, col in enumerate(row):
            if type(col) != int and type(col) != float or\
               (float(col) == float("inf")):
                raise TypeError(form)
            else:
                new_matrix[y].append(round(col / div, 2))
        length = len(row)
    return new_matrix

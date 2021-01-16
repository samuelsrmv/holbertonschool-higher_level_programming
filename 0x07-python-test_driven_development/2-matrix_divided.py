#!/usr/bin/python3
"""
Matrix Divided module
Has a function to divide matrixes
Matrix division
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.
    Matrix must be a list of integers or floats, otherwise
    will raise a TypeError.
    Each row must be the same size, otherwise will raise
    a TypeError.
    Div must be a number, otherwise, raise a TypeError.
    Div can't be zero, otherwise, ZeroDivisionError.
    All elements will be divided by div and rounded to 2 decimal places.
    Returns new matrix.
    execute: python3 -m doctest -v ./tests/2-matrix_divided.txt
    """
    new_matrix = []
    length = 0

    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if matrix == [] or matrix == [[]]:
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    if not isinstance(matrix[0], list):
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    if len(matrix[0]) <= 0:
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    for row in matrix:
        new_row = []
        if type(row) is not list:
            raise TypeError('matrix must be a matrix (list of lists) '
                            'of integers/floats')
        if length is 0:
            length = len(row)
        elif len(row) is not length:
            raise TypeError('Each row of the matrix must have the same size')
        for item in row:
            if type(item) is not int and type(item) is not float:
                raise TypeError('matrix must be a matrix (list of lists) '
                                'of integers/floats')
            if div is True or div is False:
                raise TypeError("div must be a number")
            new_row.append(round(item / div, 2))
        new_matrix.append(new_row)
    return new_matrix

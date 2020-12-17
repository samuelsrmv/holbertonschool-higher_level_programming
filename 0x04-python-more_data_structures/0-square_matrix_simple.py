#!/usr/bin/python3
def mul(x):
    return x * x


def square_matrix_simple(matrix=[]):
    tmp = []
    for x in matrix:
        tmp.append(list(map(mul, x)))
    return tmp

#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        x = 0
        for j in i:
            x = x + 1
            if x < len(i):
                print(("{:d}".format(j)), end=" ")
            else:
                print(("{:d}".format(j)), end="")
        print()

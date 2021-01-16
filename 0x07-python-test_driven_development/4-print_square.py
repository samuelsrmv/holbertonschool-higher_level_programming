#!/usr/bin/python3
"""
    prints a square with the character '#'
    execute: python3 -m doctest -v ./tests/4-print_square.txt
"""


def print_square(size):
    """
    prints a square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for x in range(size):
        print("#" * size)

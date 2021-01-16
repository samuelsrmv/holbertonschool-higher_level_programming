#!/usr/bin/python3
"""
add two numbers
execute: python3 -m doctest -v ./tests/0-add_integer.txt
"""


def add_integer(a, b=98):
    """
    functios for add two numbers
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)

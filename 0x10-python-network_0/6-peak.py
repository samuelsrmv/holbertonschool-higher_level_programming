#!/usr/bin/python3
"""function"""


def find_peak(list_of_integers):
    """pike"""
    if len(list_of_integers) == 0:
        return
    list_of_integers.sort()
    return list_of_integers[-1]

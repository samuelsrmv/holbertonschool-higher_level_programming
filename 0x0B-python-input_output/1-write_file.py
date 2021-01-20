#!/usr/bin/python3
"""module for numbers of lines
    """


def number_of_lines(filename=""):
    """return numbers of lines
    """
    with open(filename, "rt", encoding="UTF-8") as data_file:
        return (len(list(data_file)))

#!/usr/bin/python3
"""module
    """


def number_of_lines(filename=""):
    """return
    """
    with open(filename, "rt", encoding="UTF-8") as data_file:
        return (len(list(data_file)))

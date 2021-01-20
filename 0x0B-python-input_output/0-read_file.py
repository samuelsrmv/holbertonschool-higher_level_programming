#!/usr/bin/python3
"""module for read_file
    """


def read_file(filename=""):
    """read text file with utf-8
    """
    with open(filename, "r", encoding="utf-8") as file_tmp:
        data_read = file_tmp.read()
    print(data_read, end="")

#!/usr/bin/python3
"""module to write file
    """


def write_file(filename="", text=""):
    """write file with text input
    """
    with open(filename, "w", encoding="utf-8") as data_file:
        return data_file.write(text)
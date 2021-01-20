#!/usr/bin/python3
"""appends a string at the end of a text file
    """


def append_write(filename="", text=""):
    """appened string at end
    """
    with open(filename, mode="a") as data_file:
        return data_file.write(text)

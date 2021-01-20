#!/usr/bin/python3
"""
module for read_lines.
"""


def read_lines(filename="", nb_lines=0):
    """Read n lines of a text file (UTF8) and prints it to stdout."""
    count = len(open(filename).readlines())
    with open(filename, 'r') as data_file:
        if nb_lines > 0 and nb_lines < count:
            while nb_lines:
                print(data_file.readline(), end="")
                nb_lines -= 1
        else:
            read_data = data_file.read()
            print(read_data, end="")

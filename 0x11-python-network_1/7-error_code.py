#!/usr/bin/python3
"""#7"""
from sys import argv
import requests


def Eerror():
    """ function
    """
    result = requests.get(argv[1])
    if result.status_code > 400:
        print("Error code: {}".format(result.status_code))
    else:
        print(result.text)

if __name__ == "__main__":
    Eerror()

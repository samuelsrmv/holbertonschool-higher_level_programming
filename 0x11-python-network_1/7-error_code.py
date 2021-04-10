#!/usr/bin/python3
"""#7"""
import requests
import sys


def myErrorR(args):
    """what's my status"""
    try:
        x = requests.get(args)
        print(x.text)
    except requests.exceptions.HTTPError as err:
        print("Error code: {}".format(err.code))

if __name__ == "__main__":
    myErrorR(sys.argv[1])

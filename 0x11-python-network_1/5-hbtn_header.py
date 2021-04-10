#!/usr/bin/python3
"""what's my status"""
import requests
import sys


def myReque(arg):
    """what's my status"""
    x = requests.get(arg)
    print("{}".format(x.headers.get('X-Request-Id')))

if __name__ == "__main__":
    myReque(sys.argv[1])

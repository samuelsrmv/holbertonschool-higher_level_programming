#!/usr/bin/python3
"""what's my status"""
import requests
import sys


def myEmailR(args, email):
    """what's my status"""
    data = {'email': email}
    x = requests.post(args, data=data)
    print("{}".format(x.text))

if __name__ == "__main__":
    myEmailR(sys.argv[1], sys.argv[2])

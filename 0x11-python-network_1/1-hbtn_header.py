#!/usr/bin/python3
"""what's my status"""
import urllib.request
import sys

def myHeader(arg):
    """what's my status"""
    with urllib.request.urlopen(arg) as response:
        html = response.info()
        print("{}".format(html['X-Request-Id']))

if __name__ == "__main__":
    myHeader(sys.argv[1])

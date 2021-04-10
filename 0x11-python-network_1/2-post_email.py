#!/usr/bin/python3
"""what's my status"""
import urllib.request
import urllib.parse
from sys import argv


def myEmail(args, email):
    """what's my status"""
    value = {'email': email}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(args, data)
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print("{}".format(html.decode('utf-8')))

if __name__ == "__main__":
    myEmail(argv[1], argv[2])

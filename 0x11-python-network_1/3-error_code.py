#!/usr/bin/python3
"""#3"""
import urllib.request
import urllib.parse
import urllib.request,urllib.parse,urllib.error
import sys


def myError(url):
    """My Error"""
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
            print("{}".format(html.decode('utf-8')))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))

if __name__ == "__main__":
    myError(sys.argv[1])

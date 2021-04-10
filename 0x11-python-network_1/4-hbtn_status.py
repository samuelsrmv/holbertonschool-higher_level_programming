#!/usr/bin/python3
"""#4"""
import requests
import sys


def myFirstRequest():
    """My requests"""
    x = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(x.text)))
    print("\t- content: {}".format(x.text))

if __name__ == "__main__":
    myFirstRequest()

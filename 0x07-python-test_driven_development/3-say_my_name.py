#!/usr/bin/python3
""" Function thah say your name """


def say_my_name(first_name, last_name=""):
    """
    Says your name
    First ans last name must be string, otherwise will send raise a TypeError
    execute: python3 -m doctest -v ./tests/3-say_my_name.txt
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))

#!/usr/bin/python3
"""
    prints a text with 2 new lines after each of these characters: '., ?'
    execute: python3 -m doctest -v ./tests/5-text_indentation.txt
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ?
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    start = 0

    for i, c in enumerate(text):
        if i == len(text) - 1:
            print(text[start:i + 1].strip(), end="")
        elif c in ".?:":
            print(text[start:i + 1].strip(), end="\n\n")
            start = i + 1

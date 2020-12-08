#!/usr/bin/python3
def uppercase(str):
    new = ""
    for c in str:
        n = ord(c)
        if n >= 97 and n <= 122:
            n = n - 32
        cr = chr(n)
        new += cr
    print(new)

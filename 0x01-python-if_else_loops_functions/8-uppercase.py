#!/usr/bin/python3
def uppercase(str):
    for c in str:
        n = ord(c)
        if n >= 97 and n <= 122:
            n = n - 32
        cr = chr(n)
        print(cr, end="")
    print("")

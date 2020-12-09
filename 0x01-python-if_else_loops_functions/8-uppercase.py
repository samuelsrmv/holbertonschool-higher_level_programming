#!/usr/bin/python3
def uppercase(str):
    for i in str:
        n = ord(i)
        if n >= 97 and n <= 122:
            n = n - 32
        print(chr(n), end="")
    print("")

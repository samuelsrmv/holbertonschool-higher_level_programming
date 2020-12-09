#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        n = ord(str[i])
        print(chr(n), end="")
    print("")

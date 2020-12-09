#!/usr/bin/python3
def uppercase(str):
    lista = list(str)
    for i in lista:
        n = ord(i)
        if n >= 97 and n <= 122:
            n = n - 32
        print(chr(n), end="")
    print("")

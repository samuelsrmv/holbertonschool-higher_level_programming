#!/usr/bin/python3
def uppercase(str):
    l = []
    for i in str:
        n = ord(i)
        if n >= 97 and n <= 122:
            n = n - 32
        l.append(n)
    print(''.join(chr(i) for i in l))

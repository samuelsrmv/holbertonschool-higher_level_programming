#!/usr/bin/python3
x = 0
for i in range(122, 96, -1):
    print(chr(i - x), end="")
    x = 32 - x

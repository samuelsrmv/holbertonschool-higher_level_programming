#!/usr/bin/python3
for i in range(122, 96, -1):
    print(chr(i - (32 * (i % 2))), end="")
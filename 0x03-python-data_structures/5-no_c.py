#!/usr/bin/python3
def no_c(my_string):
    space = ""
    for i in my_string:
        if i != "c" and i != "C":
            space += i
    return space

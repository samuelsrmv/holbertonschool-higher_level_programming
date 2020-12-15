#!/usr/bin/python3
def no_c(my_string):
    my_string = list(my_string)
    if 'c' in my_string:
        my_string.remove("c")
    if 'C' in my_string:
        my_string.remove("C")
    return "".join(my_string)

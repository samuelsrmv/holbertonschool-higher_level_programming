#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = dict(a_dictionary)
    for x in new_dict:
        new_dict[x] = new_dict[x] * 2
    return new_dict

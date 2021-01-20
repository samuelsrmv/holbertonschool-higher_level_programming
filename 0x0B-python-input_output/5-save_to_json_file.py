#!/usr/bin/python3
"""save json file
    """


import json


def save_to_json_file(my_obj, filename):
    """write object to text file
    """
    with open(filename, mode="w") as data_file:
        data_file.write(json.dumps(my_obj))

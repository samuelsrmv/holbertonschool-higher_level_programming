#!/usr/bin/python3
"""function
    """


import json
import turtle
import random
import csv



class Base:
    """class base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """function
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

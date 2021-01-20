#!/usr/bin/python3
"""module student"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """Initialize instance student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return a dictionary representation of instance student
        """
        is_list = True
        if type(attrs) is not list:
            is_list = False
        else:
            for i in attrs:
                if type(i) is not str:
                    is_list = False

        if not is_list:
            return self.__dict__
        else:
            dicti = {}
            for attr in attrs:
                if attr in self.__dict__:
                    dicti[attr] = self.__dict__.get(attr)
            return dicti

    def reload_from_json(self, json):
        """replace all attributes of instance student
        """
        for idx, x in json.items():
            self.__dict__[idx] = x

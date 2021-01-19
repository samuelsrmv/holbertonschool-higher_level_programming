#!/usr/bin/python3
"""function that returns True if the object is an instance of a class
    """


def inherits_from(obj, a_class):
    """does this object inherit fron class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

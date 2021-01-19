#!/usr/bin/python3
"""Class BaseGeometry
    """


class BaseGeometry:
    """class BaseGeometry
    """
    def area(self):
        """area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """Rectangle
    """
    def __init__(self, width, height):
        """__init__
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("width", width)
        self.__height = height

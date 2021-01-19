#!/usr/bin/python3
"""class Rectangle
    """


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle inheirit from geometry
    """

    def __init__(self, width, height):
        """instance
        Arguments:
            width {int} -- [width fo rectangle]
            height {int} -- [height of rectangle]
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

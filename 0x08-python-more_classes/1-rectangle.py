#!/usr/bin/python3
"""class Rectangle that defines a rectangle
    """


class Rectangle:
    """class rectangle
    """

    def __init__(self, width=0, height=0):
        """Initialize rectangle
        """

        self.height = height
        self.width = width

    @property
    def height(self):
        """ Height Rectangle
        """

        return self.__height

    @height.setter
    def height(self, value):
        """ Height Rectangle
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """[summary]
        Returns:
            [type] -- [description]
        """
        return self.__width

    @width.setter
    def width(self, value):
        """[summary]
        Arguments:
            value {[type]} -- [description]
        Raises:
            TypeError: [width must be an integer]
            TypeError: [width must be >= 0]
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

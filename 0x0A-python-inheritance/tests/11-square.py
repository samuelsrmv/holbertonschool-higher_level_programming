#!/usr/bin/python3
"""class Square
    """


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ class squares
    """

    def __init__(self, size):
        """initialize a square
        Arguments:
            size {int}
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """return str
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)

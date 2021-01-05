#!/usr/bin/python3
"5-square.py define"


class Square:
    """class Square
    """

    def __init__(self, size=0):
        """Inizialitation of variables
        Arg self identificador
        size of square
        """
        self.size = size

    @property
    def size(self):
        """Inizialitation of variables
        Arg self identificador
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Inizialitation of variables
        Arg self identificador
        value of square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise valueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Inizialitation of variables
        Arg self identificador
        """
        return self.__size ** 2

    def my_print(self):
        """Inizialitation of variables
        Arg self identificador
        """
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                print("#" * self.__size)

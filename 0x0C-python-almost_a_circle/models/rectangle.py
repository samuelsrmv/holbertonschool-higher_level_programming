#!/usr/bin/python3
"""Rectangle base
    """


from models.base import Base


class Rectangle(Base):
    """class rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes instance rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter function to return instance private attribute __width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter functión for private instance attribute __width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter function to return instance private attribute __height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter functión for private instance attribute __height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter function to return instance private attribute __x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """setter functión for private instance attribute __x
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter function to return instance private attribute __y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """setter functión for private instance attribute __y
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        task 4
        methods public that return rectangle area
        """
        return self.__width * self.__height

    def display(self):
        """
        task 5 - 6 -7
        methods public that print in stdout  the rectangle instance
        """

        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print("{:s}{:s}".format(" " * self.__x, "#" * self.__width))

    def __str__(self):
        """
        task 6
        print a rectangle instance
        """
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        task 8 - 9
        update class rectangle with args and kwargs
        """
        i = 0
        if args and len(args) > 0:
            for idx in args:
                if i == 0:
                    self.id = idx
                elif i == 1:
                    self.__width = idx
                elif i == 2:
                    self.__height = idx
                elif i == 3:
                    self.__x = idx
                elif i == 4:
                    self.__y = idx
                else:
                    break
                i += 1
        else:
            for idx in kwargs:
                if idx == "id":
                    self.id = kwargs[idx]
                if idx == "width":
                    self.__width = kwargs[idx]
                if idx == "height":
                    self.__height = kwargs[idx]
                if idx == "x":
                    self.__x = kwargs[idx]
                if idx == "y":
                    self.__y = kwargs[idx]

    def to_dictionary(self):
        """return dictionary of the atributes rectangle
        """
        array = ["id", "width", "height", "x", "y"]
        dict = {}
        for idx in array:
            dict.update({idx: getattr(self, idx)})
#!/usr/bin/python3
"""class square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Squiare
    """
    def __init__(self, size, x=0, y=0, id=None):
        """constructor
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        __str__
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
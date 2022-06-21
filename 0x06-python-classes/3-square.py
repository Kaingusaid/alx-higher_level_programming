#!/usr/bin/python3
""" Private instance attribute: size """


class Square:
    """ The instance attribute must be integer. Raise TypeError: if
    size is not an integer & ValueError: if size is less than zero
    """
    def __init__(self, size=0):
        """ initializing the instance size """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size


    def area(self):
        return self.__size ** 2

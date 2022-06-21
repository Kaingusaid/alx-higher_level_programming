#!/usr/bin/python3
""" Private instance attribute """


class Square:
    """ The instance will have property to retrieve it and set it
    The instance size must be an integer, hence, raise TypeError if
    otherwise and ValueError if size is less than 0 """
    def __init__(self, size=0):
        """ Initializing the attribute """
        self.__size = size


    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        """ Getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

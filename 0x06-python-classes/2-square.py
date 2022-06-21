#!/usr/bin/python3
""" Initializing private instance """


class Square:
    """ private instance attribute: size
    The instance must be an integer. Raise error: TypeError & ValueError
    """
    def __init__(self, size=0):
        """ Initializing the size """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

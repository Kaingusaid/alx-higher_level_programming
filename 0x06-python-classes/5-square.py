#!/usr/bin/python3
""" Private instance attribute """


class Square:
    """ The size attribute must be an integer. A TypeError is raised
    if size is otherwise and a ValueError is raised if size is less
    than zero
    """
    def __init__(self, size=0):
        """ Initializing the attribute """
        self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        """ getter """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """ Printing # if true and empty space if false """
        if self.__size == 0:
            print("")
        for char in range(0, self.__size):
            for symbol in range(0, self.__size - 1):
                print("#", end="")
            print("#")

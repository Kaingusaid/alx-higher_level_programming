#!/usr/bin/python3


"""
importing Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square inheriting class Rectangle
    """

    def __init__(self, size):
        """
         function for class square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        calculating area
        """
        return self.__size ** 2

    def __str__(self):
        """
        finding the size
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

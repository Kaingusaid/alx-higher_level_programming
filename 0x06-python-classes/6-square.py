#!/usr/bin/python3
"""Writing class Square that defines a square by using attribute, try/except"""


class Square:
    """Class Square that defines a square using an private attribute.
    Attributes:
        size: private attribute to define square with
    """
    def __init__(self, size=0, position=(0, 0)):
        """Instantiation of size and position
        Args:
            size: attribute
            position: attribute
        """
        if not isinstance(position, tuple) or len(position) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[1] < 0 or position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """Position's getter
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Position's setter
        """
        if not isinstance(value, tuple) or len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[1] < 0 or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returning square area
        """
        return self.__size ** 2

    @property
    def size(self):
        """Getter
        """
        return self.__size

    @size.
    def size(self, value):
        """setter
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Printing # if true or empty space if false
        """
        if self.__size == 0:
            print("")
        else:
            for sym in range(0, self.position[1]):
                print("")
            for sym in range(0, self.__size):
                for char in range(0, self.position[0]):
                    print(" ", end="")
                for char in range(0, self.__size - 1):
                    print("#", end="")
                print("#")

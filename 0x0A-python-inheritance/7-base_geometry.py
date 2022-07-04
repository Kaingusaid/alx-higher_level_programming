#!/usr/bin/python3


"""
Creating a class
"""


class BaseGeometry:
    """
    created  a class BaseGeometry
    """

    def area(self):
        """
        public instance method for class BaseGeometry
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        public instance method to validate value
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")

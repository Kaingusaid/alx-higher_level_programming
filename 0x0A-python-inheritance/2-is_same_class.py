#!/usr/bin/python3


"""
creating a function
"""


def is_same_class(obj, a_class):
    """
    check if the object is of specified class
    """

    if type(obj) == a_class:
        return True
    else:
        return False

#!/usr/bin/python3


"""
writing a funtion
"""


def inherits_from(obj, a_class):
    """
    prototype for the function
    """
    if type(obj) != a_class and isinstance(obj, a_class):
        return True
    else:
        return False

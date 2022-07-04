#!/usr/bin/python3


"""
writing a function
"""


def is_kind_of_class(obj, a_class):
    """
    prototype for the function
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False

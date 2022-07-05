#!/usr/bin/python3


"""
creating an attribute
"""


def add_attribute(object, attribute, value):
    """
    defined add_attribute
    """
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, attribute, value)

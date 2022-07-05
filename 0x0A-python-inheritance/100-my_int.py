#!/usr/bin/python3


"""
creating a class Int
"""


class MyInt(int):
    """
    class MyInt inheriting class int
    """
    def __eq__(self, other):
        return False

    def __ne__(self, other):
        return True

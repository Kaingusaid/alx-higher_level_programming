#!/usr/bin/python3


"""
defining a child class
"""


class MyList(list):
    """
    defined a child class that inherits the parent class list
    """

    def print_sorted(self):
        print(sorted(self))

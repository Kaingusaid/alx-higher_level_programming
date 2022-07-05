#!/usr/bin/python3


"""
function that reads a text file
"""


def read_file(filename=""):
    """
    prototype for the function to read file
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

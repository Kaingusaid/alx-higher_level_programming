#!/usr/bin/python3


"""
creating a function that writes a string to a text file
"""


def write_file(filename="", text=""):
    """
    prototype for the function
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
        return len(text)

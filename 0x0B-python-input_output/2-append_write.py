#!/usr/bin/python3
"""Appends a string of a text file"""


def append_write(filename="", text=""):
    """Appends a string of a text file"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)

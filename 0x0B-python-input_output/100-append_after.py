#!/usr/bin/python3
""" Search and update"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file"""
    with open(filename, 'r', encoding='utf-8') as f:
        wi = f.readlines()
    with open(filename, "w", encoding="utf-8") as f:
        for a in wi:
            f.write(a)
            if (search_string in a):
                f.write(new_string)

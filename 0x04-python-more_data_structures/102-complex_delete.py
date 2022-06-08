#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for (l, e) in dict(a_dictionary).items():
        if e is value:
            a_dictionary.pop(l, None)
    return a_dictionary

#!/usr/bin/python3
def no_c(my_string):
    my_chars = ['c', 'C']
    new_string = ''.join(i for i in my_string if i not in my_chars)
    return new_string

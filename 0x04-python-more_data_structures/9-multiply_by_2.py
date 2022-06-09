#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_d = {}
    for z in a_dictionary:
        new_d[z] = a_dictionary[z] * 2
    return new_d

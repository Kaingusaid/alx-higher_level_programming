#!/usr/bin/python3
def weight_average(my_list=[]):
    add = 0
    weight = 0
    if len(my_list) == 0:
        return 0
    for num in my_list:
        add += num[0] * num[1]
        weight += num[1]
    return add / weight

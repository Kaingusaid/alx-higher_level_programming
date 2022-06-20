#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    element = 0
    for num in range(0, x):
        try:
            print("{}".format(my_list[num]), end="")
            element = element + 1
        except:
            pass
    print("")
    return element

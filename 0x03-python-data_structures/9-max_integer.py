#!/usr/bin/python3

def max_integer(my_list=[]):
    # function finds the biggest integer in a list
    if len(my_list) == 0:
        return None
    valMax = my_list[0]

    for i in my_list[1:]:
        if i > valMax:
            valMax = i
    return valMax

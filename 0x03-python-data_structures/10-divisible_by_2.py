#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    # function finds all the multiples of 2 in a list

    if len(my_list) == 0:
        return None
    new_list = []
    for n in my_list:
        if n % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list

#!/usr/bin/python3

def common_elements(set_1, set_2):
    # function returns a set of common elements in two set
    # this can be done using the & which is also the
    # intersection() function. also it can be done using the
    # set() function too. but i would use a different an more
    # longer approach
    same_elements_in_set = []
    for elements in set_1:
        if elements in set_2:
            same_elements_in_set.append(elements)
    return same_elements_in_set

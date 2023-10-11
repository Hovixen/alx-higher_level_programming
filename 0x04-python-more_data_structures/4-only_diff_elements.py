#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    # function returns a set of elements present in only one set
    # you can use symetric difference or the ^ sign operator
    inset_1 = []
    inset_2 = []
    for elements in set_1:
        if elements not in set_2:
            inset_1.append(elements)
    for elements in set_2:
        if elements not in set_1:
            inset_2.append(elements)
    return (list(inset_1 + inset_2))

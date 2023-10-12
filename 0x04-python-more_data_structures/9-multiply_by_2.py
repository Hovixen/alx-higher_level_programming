#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    # function returns a new dictionary with all values multiplied by 2
    new_dic = a_dictionary.copy()
    # i represents the key of the dictionary
    for i in new_dic:
        new_dic[i] *= 2
    return (new_dic)

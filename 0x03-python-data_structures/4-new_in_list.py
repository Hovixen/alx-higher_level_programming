#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    # function replaces an element in a list at a specific location
    # without modifying the original list
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        list_new = my_list[:]
        list_new[idx] = element
        return list_new

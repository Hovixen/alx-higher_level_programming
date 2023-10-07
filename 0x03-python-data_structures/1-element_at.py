#!/usr/bin/python3

def element_at(my_list, idx):
    # function retrieves an element at a position in a list
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        return my_list[idx]

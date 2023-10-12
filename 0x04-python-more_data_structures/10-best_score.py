#!/usr/bin/python3

def best_score(a_dictionary):
    # function returns a key with the biggest integer value
    # this can also be simplified using the max() function
    # or using a comprehension method
    if a_dictionary is None:
        return None
    maxval = float('-inf')
    maxkey = None
    for key, value in a_dictionary.items():
        if value > maxval:
            maxval = value
            maxkey = key
    return maxkey

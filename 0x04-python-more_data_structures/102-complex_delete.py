#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    # function deletes keys with a specific value in a dictionary
    key_to_del = []
    for keys, values in a_dictionary.items():
        if values == value:
            key_to_del.append(keys)
    for i in key_to_del:
        del a_dictionary[i] 

    return (a_dictionary)

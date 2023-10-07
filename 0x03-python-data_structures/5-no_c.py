#!/usr/bin/python3

def no_c(my_string):
    # function removes all c and C from string
    string = ''
    for i in my_string:
        if i != 'c' and i != 'C':
            string += i
    return string

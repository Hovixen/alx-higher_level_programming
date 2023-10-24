#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=[]):
    # function prints the first x element of a list and only integers
    # n keeps track of the elements printed
    n = 0
    try:
        for i in range(x):
            element = my_list[i]
            try:
                print('{:d}'.format(element), end='')
                n += 1
            except (ValueError, TypeError):
                pass
        print()
        return n
    except TypeError:
        return n

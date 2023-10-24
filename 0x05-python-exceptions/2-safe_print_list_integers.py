#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=[]):
    # function prints the first x element of a list and only integers
    # n keeps track of the elements printed
    n = 0
    try:
        for i in my_list:
            if n < x:
                try:
                    print('{:d}'.format(i), end='')
                    n += 1
                except (ValueError, TypeError):
                    pass
        print()
        return n
    except (TypeError):
        return n

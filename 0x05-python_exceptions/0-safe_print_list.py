#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    # function prints x element of a list
    # n tracks the printed elements
    n = 0
    try:
        for i in my_list:
            if n < x:
                print('{}'.format(i), end='')
                n += 1
        print()
        return n
    except:
        return n

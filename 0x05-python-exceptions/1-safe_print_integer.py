#!/usr/bin/python3

def safe_print_integer(value):
    # function that prints and integer

    try:
        print('{:d}'.format(value))
    except (TypeError, ValueError):
        return False
    else:
        return True

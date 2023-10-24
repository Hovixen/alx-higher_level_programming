#!/usr/bin/python3

def safe_print_division(a, b):
    # function divides two integer and prints the result

    try:
        ans = a / b
    except ZeroDivisionError:
        ans None
    finally:
        print("Inside result: {}".format(ans))
        return ans

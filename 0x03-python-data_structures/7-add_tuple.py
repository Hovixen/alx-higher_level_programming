#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # use slice to get the first two element
    a = tuple_a[:2]
    b = tuple_b[:2]
    # fill the missing element with 0
    while len(a) < 2:
        a += (0,)
    while len(b) < 2:
        b += (0,)
    # get the sum of the tuple
    sum_tuple = (a[0] + b[0], a[1] + b[1])
    return sum_tuple

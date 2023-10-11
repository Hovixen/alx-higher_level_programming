#!/usr/bin/python3

def uniq_add(my_list):
    # function adds all unique integers in a list(only once for each integer)
    # i can use the built-in function set() to easily pick out all the unique
    # numbers and use the sum() function to add them all
    # but here i used a differenct approach
    once_occur = []
    sums = 0
    for i in my_list:
        if i not in once_occur:
            once_occur.append(i)
            sums += i
    return sums


#!/usr/bin/python

def print_matrix_integer(matrix=[[]]):
    # function prints a matrix of integers
    for i in matrix:
        for j in i:
            if j != 0:
                print(' ', end='')
            print('{:d}'.format(j), end='')
        print()

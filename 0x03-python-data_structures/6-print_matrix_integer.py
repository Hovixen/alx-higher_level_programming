#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    # function prints matrix of integer
    for row in matrix:
        for i, column in enumerate(row):
            print('{:d}'.format(column), end=' ' if i < len(row) - 1 else '')
        print()

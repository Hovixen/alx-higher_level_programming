#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    # function prints matrix of integer
    for row in matrix:
        for col in range(len(row)):
            print('{:d}'.format(row[col]), end=' ' if col < len(row) - 1 else '')
        print()

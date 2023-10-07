#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    # function prints matrix of integer
    for row in matrix:
        for column in range(len(row)):
            print('{:d}'.format(row[column]), end=' ' if column < len(row) - 1 else '')
        print()

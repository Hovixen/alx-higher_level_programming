#!/usr/bin/python

def print_matrix_integer(matrix=[[]]):
    # function prints a matrix of integers
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if column != 0:
                print(' ', end='')
            print('{:d}'.format(matrix[row][column]), end='')
        print()

#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # function computes the square value of all integers of a matrix
    # Mrow is the rows in the Matrix
    # e is the elements in the Matrix row
    matrixNew = list(map(lambda M.R: list(map(lambda e: e ** 2, M.R)), matrix))
    return matrixNew

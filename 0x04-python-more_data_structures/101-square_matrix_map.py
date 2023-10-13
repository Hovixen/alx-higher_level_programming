#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda R: list(map(lambda e: e ** 2, R)), matrix))

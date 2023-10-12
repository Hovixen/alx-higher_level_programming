#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return (list(map(lambda M_R: list(map(lambda e: e ** 2, M_R)), matrix)))

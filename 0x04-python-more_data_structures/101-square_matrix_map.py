#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(list(map(lambda x: x ** 2, elt)) for elt in matrix)
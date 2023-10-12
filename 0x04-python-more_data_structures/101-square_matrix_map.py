#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_matrix = list(map((lambda elt: list(map((lambda x: x * x), elt))), matrix))
    return new_matrix

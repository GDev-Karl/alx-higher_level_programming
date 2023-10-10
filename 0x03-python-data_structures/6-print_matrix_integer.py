#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for elt in row:
            if elt == row[-1]:
                print("{:d}".format(elt), end="")
            else:
                print("{:d}".format(elt), end=" ")
        print()

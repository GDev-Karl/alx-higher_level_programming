#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = 0
    for elt in set(my_list):
        unique += elt

    return unique

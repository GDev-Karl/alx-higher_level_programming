#!/usr/bin/python3
def element_at(my_list, idx):
    for i, elt in enumerate(my_list):
        if i == idx:
            return elt

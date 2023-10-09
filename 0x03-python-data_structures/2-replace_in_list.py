#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    new_list = my_list
    for i, elt in enumerate(new_list):
        if i == idx:
            new_list[i] = element
    return new_list

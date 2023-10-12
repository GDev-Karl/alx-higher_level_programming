#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if elt == search else elt for elt in my_list]

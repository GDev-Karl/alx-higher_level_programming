#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    divisible = [elt % 2 == 0 for elt in my_list]
    return divisible

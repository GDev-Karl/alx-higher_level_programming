#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    weight = 0
    average = 0
    for key, value in my_list:
        average += key * value
        weight += value

    return average / weight

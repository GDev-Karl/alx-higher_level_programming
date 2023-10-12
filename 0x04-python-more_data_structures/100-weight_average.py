#!/usr/bin/python3
def weight_average(my_list=[]):
    weight = 0
    average = 0
    for key, value in my_list:
        average += key * value
        weight += value
        
    return average / weight

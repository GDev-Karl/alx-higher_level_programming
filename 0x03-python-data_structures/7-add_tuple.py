#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tple1 = tuple_a + (0, 0)
    tple2 = tuple_b + (0, 0)

    result = tple1[0] + tple2[0], tple1[1] + tple2[1]
    return result

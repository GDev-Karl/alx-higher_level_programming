#!/usr/bin/python3
"""Operation Module """

def add_integer(a, b=98):

    """
    add two iteger
    
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

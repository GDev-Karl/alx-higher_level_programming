#!/usr/bin/python3
"""Operation Module """

def add_integer(a, b=98):
    
    """
    add two iteger
    """
    if not isinstance(a, (int, float)) and not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    return int(a) + int(b)
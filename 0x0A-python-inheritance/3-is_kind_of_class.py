#!/usr/bin/python3
""" Module of instance """


def is_kind_of_class(obj, a_class):
    """
    returns true if object is an instance of a class
    that this class inherits from
    """
    return (isinstance(obj, a_class))

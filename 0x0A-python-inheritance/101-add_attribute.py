#!/usr/bin/python3
""" Add Attributes """


def add_attribute(obj, att, value):
    """
    Adding of attribute to an object if possible
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)

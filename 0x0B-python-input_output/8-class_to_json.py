#!/usr/bin/python3
""" Module on JSON """
import json


def class_to_json(obj):
    """
    returns the dictionary description with simple data structure
    for JSON serialization of an object
    """
    return vars(obj)

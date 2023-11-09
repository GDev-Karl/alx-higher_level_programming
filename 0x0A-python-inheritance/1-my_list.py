#!/usr/bin/python3
""" Module of inheritance """


class MyList(list):
    """
    class MyList that inherits from list
    """
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))

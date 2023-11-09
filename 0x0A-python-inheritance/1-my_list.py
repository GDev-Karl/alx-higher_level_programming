#!/usr/bin/python3
""" Module of inheritance """


class MyList(list):
    """
    A class that inherits from list
    """

    def print_sorted(self):
        print(sorted(self))

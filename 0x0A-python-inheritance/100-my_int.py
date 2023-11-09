#!/usr/bin/python3
"""Inheritance from int class"""


class MyInt(int):
    """Invert int operators == and !="""

    def __eq__(self, value):
        """
        == opeartor inverted
        """
        return self.real != value

    def __ne__(self, value):
        """
        != opeartor inverted
        """
        return self.real == value

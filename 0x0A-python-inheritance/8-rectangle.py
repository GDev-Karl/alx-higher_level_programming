#!/usr/bin/python3
"""Inheris from baseGeometry"""


class Rectangle(BaseGeometry):
    """define a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """
        Intialization
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

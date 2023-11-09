#!/usr/bin/python3
"""Inheris from baseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """define a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """
        Intialization
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """str representation of a Rectangle"""
        rep = "[" + str(self.__class__.__name__) + "] "
        rep += str(self.__width) + "/" + str(self.__height)
        return rep

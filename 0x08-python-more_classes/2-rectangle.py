#!/usr/bin/python3
""" Rectangle module """


class Rectangle:
    """ defines rectangle """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        retrieves width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set the value of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        retrieves height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        set the value of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        returns the rectangle area
        """
        return self.width * self.height

    def perimeter(self):
        """
        returns the rectangle perimeter
        """
        if self.width == 0 and self.height == 0:
            return 0
        return (self.width + self.height) * 2

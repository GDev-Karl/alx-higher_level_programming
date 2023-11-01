#!/usr/bin/python3
""" Rectangle module """


class Rectangle:
    """ defines rectangle """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self) -> str:
        """
        print the rectangle with the character #
        """
        if self.width == 0 or self.height == 0:
            return ""

        rectangle = ""
        for y in range(self.height):
            for x in range(self.width):
                rectangle += "#"
            if y < self.height - 1:
                rectangle += "\n"

        return rectangle

    def __repr__(self) -> str:
        """
        string representation of the rectangle
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """
        Print a message when the object is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

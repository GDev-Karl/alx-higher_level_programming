#!/usr/bin/python3
""" Inheritance from restangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square inherits from Rectangle"""

    def __init__(self, size):
        """
        Initialization
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size 

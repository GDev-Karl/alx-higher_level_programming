#!/usr/bin/python3
# 0-square.py by Leonard Odoi
""" Defines a square """


class Square:
    """ Square """

    def __init__(self, size=0):
        """
        Args:
            size:the size of the square
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """get the size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size of square"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Returns: The area of the square
        """

        return (self.__size ** 2)

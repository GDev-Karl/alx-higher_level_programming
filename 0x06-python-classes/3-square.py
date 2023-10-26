#!/usr/bin/python3
""" Define fines a square """


class Square:
    """ Square """

    def __init__(self, size=0):
        """
        Args:
            size: he size of the square
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        Returns: The area of the square
        """

        return (self.__size ** 2)

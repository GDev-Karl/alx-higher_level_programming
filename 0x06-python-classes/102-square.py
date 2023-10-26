#!/usr/bin/python3
""" Defines a square """


class Square:
    """Square"""

    def __init__(self, size=0):
        """Create a Square
        Args: size: length of a side of Square
        """
        self.__size = size

    @property
    def size(self):
        """
        Args:
            size: a side of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        set the size of square
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Returns: The area of the square
        """
        return self.__size * self.__size

    def __le__(self, other):
        return self.area() <= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __eq__(self, other):
        return self.area() == other.area()
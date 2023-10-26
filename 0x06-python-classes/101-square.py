#!/usr/bin/python3
""" Defines a square """


class Square:
    """Square."""

    def __str__(self):
        """
        print the square my way
        """
        return self.pos_print()[:-1]

    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            size: a side of square
            position: square coordonates
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        get the size of square
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

    @property
    def position(self):
        """
        get the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        set the size of square
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """
        Returns: The area of the square
        """
        return self.__size * self.__size

    def pos_print(self):
        """
        returns the position in spaces
        """
        pos = ""
        if self.size == 0:
            return "\n"
        for i in range(self.position[1]):
            pos += "\n"
        for j in range(self.size):
            for x in range(self.position[0]):
                pos += " "
            for y in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """
        print the square in position
        """
        print(self.pos_print(), end='')

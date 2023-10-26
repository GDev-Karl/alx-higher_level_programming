#!/usr/bin/python3
""" Defines a square """


class Square:
    """ Square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            size:the size of the square
            position: square coordonates
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
        self.position = position

    def __str__(self):
        self.my_print()

    @property
    def size(self):
        """get the size of square"""

        return self.__size

    @property
    def position(self):
        """get the position of square"""

        return self.__position

    @position.setter
    def position(self, value):
        """set the position of Square
        Args: positon as a tuple
        """

        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')

    def pos_print(self):
        """print and return the position of the square """

        pos = ""
        if self.size == 0:
            return "\n"
        for i in range(self.position[1]):
            pos += "\n"
            pos += " "
            for k in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

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

    def my_print(self):
        """print the square in # """

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)

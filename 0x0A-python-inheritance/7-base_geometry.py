#!/usr/bin/python3
""" Module Base Geometry"""


class BaseGeometry:
    """define a base geometry"""

    def area(self):
        """ area of the figure """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates a value as an integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

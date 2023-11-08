#!/usr/bin/python3
""" Module on JSON """


class Student:
    """
    Define a student
    """
    def __init__(self, first_name, last_name, age):
        """
        new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        dictionary representation of the Student
        """
        return self.__dict__

#!/usr/bin/python3
""" Student module """


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

    def to_json(self, attrs):
        """
        dictionary representation of the Student
        """
        if (isinstance(list, attrs) and
                all(isinstance(str, elt) for elt in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.

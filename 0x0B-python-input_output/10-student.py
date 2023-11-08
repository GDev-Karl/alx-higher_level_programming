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

    def to_json(self, attrs = None):
        """
        dictionary representation of the Student
        """
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        
        return self.
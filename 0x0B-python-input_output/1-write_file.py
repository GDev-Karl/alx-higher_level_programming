#!/usr/bin/python3
""" Module on file """


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8) and returns the number of characters
    """
    with open(filename, "w") as f:
        return f.write(text)

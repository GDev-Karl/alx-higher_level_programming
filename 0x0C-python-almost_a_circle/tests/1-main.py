#!/usr/bin/python3
""" test the rectangle class """
from models.rectangle import Rectangle

if __name__ == "__main__":

    rect1 = Rectangle(10, 2)
    print(rect1.id)

    rect2 = Rectangle(2, 10)
    print(rect2.id)

    rect3 = Rectangle(10, 2, 0, 0, 12)
    print(rect3.id)

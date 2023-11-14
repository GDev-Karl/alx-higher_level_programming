#!/usr/bin/python3
""" test the base class """
from models.base import Base

if __name__ == "__main__":

    bs1 = Base()
    print(bs1.id)

    bs2 = Base()
    print(bs2.id)

    bs3 = Base()
    print(bs3.id)

    bs4 = Base(12)
    print(bs4.id)

    bs5 = Base()
    print(bs5.id)

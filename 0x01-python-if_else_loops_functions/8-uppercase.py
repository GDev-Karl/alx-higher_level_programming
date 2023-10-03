#!/usr/bin/python3

def uppercase(str):
    new_str = ""
    for char in str:
        if (ord(char) in range(ord('a'), ord('z') + 1)):
            char = chr(ord(char) - 32)
        new_str = new_str + char

    print("{}".format(new_str))

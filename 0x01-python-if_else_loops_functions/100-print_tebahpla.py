#!/usr/bin/python3

def upper(number):
    if (number in range(ord('a'), ord('z') + 1)):
        return (number - 32)


for char_code in range(ord('z'), ord('a') - 1, -1):
    if char_code % 2 == 0:
        print("{:c}".format(char_code), end="")
    else:
        print("{:c}".format(upper(char_code)), end="")

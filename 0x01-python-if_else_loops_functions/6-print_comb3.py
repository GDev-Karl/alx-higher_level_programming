#!/usr/bin/python3

for dgt_1 in range(10):
    for dgt_2 in range(dgt_1 + 1, 10):
        if dgt_1 == 8 and dgt_2 == 9:
            print("{}{}".format(dgt_1, dgt_2))
        else:
            print("{}{}, ".format(dgt_1, dgt_2), end="")

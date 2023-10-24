#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    number = 0

    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            number += 1
        except Exception:
            break
    print()
    return number

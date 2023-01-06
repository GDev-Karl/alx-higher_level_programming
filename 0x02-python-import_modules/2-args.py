#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    cpt = len(sys.argv) - 1
    if cpt == 0:
        print("0 arguments.")
    elif cpt == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i in range(cpt):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
            
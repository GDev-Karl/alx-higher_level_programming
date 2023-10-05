#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    nb_agrs = len(argv) - 1

    if nb_agrs == 0:
        print("{} arguments.".format(nb_agrs))
    else:
        if nb_agrs == 1:
            print("{} argument:".format(nb_agrs))
        else:
            print("{} arguments:".format(nb_agrs))

    for i in range(nb_agrs):
        print("{}: {}".format(i + 1, argv[i + 1]))

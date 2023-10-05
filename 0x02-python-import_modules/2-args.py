#!/usr/bin/python3
from sys import argv

nb_agrs = len(argv) - 1

if nb_agrs == 0:
    print("0 arguments.")
else:
    if nb_agrs == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(nb_agrs))

    for i in range(nb_agrs):
        print("{}: {}".format(i + 1, argv[i + 1]))

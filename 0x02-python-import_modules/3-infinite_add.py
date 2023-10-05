#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    nb_agrs = len(argv) - 1
    sum = 0

    for i in range(nb_agrs):
        sum = sum + int(argv[i + 1])

    print(sum)

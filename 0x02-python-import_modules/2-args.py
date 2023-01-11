#!/usr/bin/python3

if __name__ == "__main__":
    import sys
count = len(sys.argv) - 1

if count == 0:
    print("{} arguments.".format(count))
else
    if count == 1:
        print("{} argument:".format(count))
    else:
        print("{} arguments:".format(count))
    for i in range(1, count + 1):
        print("{}: {}".format(i , sys.argv[i]))
            
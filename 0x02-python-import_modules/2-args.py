#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    n = len(sys.argv) - 1
    if n == 0:
        print("{} arguments.".format('0'))
    elif n == 1:
        print("{} arguments:".format('n'))
    else:
        print("{} arguments:".format(n))
    for index in range(n):
        print("{}: {}".format(index + 1, sys.argv[index + 1]))

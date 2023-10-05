#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arge = len(sys.argv)-1
    if arge == 0:
        print("0 arguments.")
    elif arge == 1:
        print("1 argumenst:")
    else:
        print("{} arguments:".format(arge))

    for i in range(arge):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))


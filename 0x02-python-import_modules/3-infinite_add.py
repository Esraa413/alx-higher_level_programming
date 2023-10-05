#!/usr/bin/python3
import sys
if __name__ == "__main__":
    total = 0
    for x in range(len(sys.argv) - 1):
        total += int(sys.argv[x + 1])
    print("{}".format(total))

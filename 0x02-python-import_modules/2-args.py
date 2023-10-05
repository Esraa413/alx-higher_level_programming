#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arge = len(sys.argv)-1
    if arge == 0:
        print("0 arguments:")
    elif arge == 1:
        print("1 argumenst:")
    else:
        print(f"{arge} arguments:")

    for x in range(arge):
        print(f"{x + 1} : {sys.argv[x + 1]}")


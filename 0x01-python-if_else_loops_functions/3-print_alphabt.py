#!/usr/bin/python3

for ascll in range(97, 123):
    if chr(ascll) not in 'e' and chr(ascll) not in 'q':
        print("{}".format(chr(ascll)), end="")

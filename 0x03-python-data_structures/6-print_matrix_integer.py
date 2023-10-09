#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for num in matrix:
        for num2 in num:
            print("{:d}".format(num2), end=" " if num2 != num[-1] else "")
        print()

#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print x of list

    Args:
        my_list (list): print elements.
        x (int): number of elements to my_list.

    Return:
        number of elements.
    """

    new = 0
    for y in range(0, x):
        try:
            print("{:d}".format(my_list[y]), end="")
            new += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (new)

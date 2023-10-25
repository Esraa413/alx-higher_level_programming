#!/usr/bin/python3
def safe_print_integer(value):
    """function that prints an integer with "{:d}".format().

    Args:
        value (int): any type (integer, string, etc.)

    Returns:
        ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)

#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """function that divides element by element 2 lists.

    Args:
        my_list_1 (list): first list.
        my_list_2 (list): second list.
        list_length (int): length number to divide
    
    Return:
        new list of length, containing all the divisions.
    """

    list3 = []
    for x in range(0, list_length):
        try:
            div = my_list_1[x] / my_list_2[x]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            list_3.append(div)

    return (list3)

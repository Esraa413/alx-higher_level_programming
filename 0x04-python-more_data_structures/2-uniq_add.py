#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_num = set(my_list)
    number = 0
    for x in uniq_num:
        number += x
    return (number)

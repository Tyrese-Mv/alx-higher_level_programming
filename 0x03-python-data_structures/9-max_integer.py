#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    checkMax = my_list[0]
    for element in range(len(my_list)):
        if my_list[element] > checkMax:
            checkMax = my_list[element]
    return checkMax

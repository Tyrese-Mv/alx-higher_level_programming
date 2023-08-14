#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) != 0:
        my_list.reverse()
        for number in range(len(my_list)):
            print("{:d}".format(my_list[number]))

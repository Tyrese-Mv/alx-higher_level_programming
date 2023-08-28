#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
        return i
    except IndexError:
        i = 0
        for item in my_list:
            print("{}".format(item), end="")
            i++
        return i

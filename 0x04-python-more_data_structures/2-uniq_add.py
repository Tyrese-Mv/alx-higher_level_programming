#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_num = set()
    total = 0
    for element in my_list:
        if element not in uniq_num:
            total += element
            uniq_num.add(element)
    return total

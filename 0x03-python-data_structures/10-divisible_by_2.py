#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newList = []
    for index in range(len(my_list)):
        if my_list[index] % 2 == 0:
            newList.append(True)
        else:
            newList.append(False)
    return newList

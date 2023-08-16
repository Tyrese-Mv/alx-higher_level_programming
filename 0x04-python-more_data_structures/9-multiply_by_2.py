#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for x, y in a_dictionary.items():
        a_dictionary[x] = y * 2
    return a_dictionary

#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for x, y in a_dictionary.items():
        new_dictionary[x] = y * 2
    return new_dictionary

#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    elements_set_1 = [x for x in set_1 if x not in set_2]
    elements_set_2 = [x for x in set_2 if x not in set_1]
    element = elements_set_1 + elements_set_2
    return element

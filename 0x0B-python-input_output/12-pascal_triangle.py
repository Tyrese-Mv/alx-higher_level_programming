#!/usr/bin/python3
"""Pascal triangle"""


def fact(n):
    """ factorial
    Arg:
        n: number to factorise
    """
    if n == 0:
        return 1
    return n * fact(n - 1)


def pascal_triangle(n):
    """pascal triangle
        Arg:
        n: Number of lists
    """
    if n <= 0:
        return []
    row_list = []
    for level in range(n + 1):
        new_list = []
        for column in range(level + 1):
            element = fact(level) / (fact(column) * fact(level - column))
            new_list.append(element)
        row_list.append(new_list)
    return row_list

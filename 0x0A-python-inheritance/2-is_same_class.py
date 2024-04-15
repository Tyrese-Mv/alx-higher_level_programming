#!/usr/bin/python3

"""checks instance of an object"""


def is_same_class(obj, a_class):

    """checks if object matches exactly it's class"""

    if isinstance(obj, a_class) and type(obj) == a_class:
        return True
    return False

#!/usr/bin/python3

"""instance of an object"""


def inherits_from(obj, a_class):
    """check instance of an object"""

    return isinstance(obj, a_class) and type(obj) != a_class

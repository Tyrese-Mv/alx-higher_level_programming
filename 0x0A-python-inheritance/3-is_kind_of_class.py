#!/usr/bin/python3
"""instance of an object"""
def is_kind_of_class(obj, a_class):
    """check instance of an object"""
    if isinstance(obj, a_class):
        return True
    return False

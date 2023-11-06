#!/usr/bin/python3
"""adding attribute"""


def add_attribute(obj, name, value):
    """adding new attribute
    Args:
        obj: object
        name: attribute name
        value: attribute value"""
    if hasattr(obj, '__dict__') or (hasattr(obj, '__slot__') and name in obj.__slots__):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")

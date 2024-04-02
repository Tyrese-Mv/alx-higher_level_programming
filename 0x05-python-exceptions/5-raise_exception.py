#!/usr/bin/python3
def raise_exception():
    name = "Musa"
    try:
        result = int(name)
    except:
        raise TypeError("")

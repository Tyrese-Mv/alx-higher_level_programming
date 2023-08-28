#!/usr/bin/python3
def safe_print_integer(value):
    ifHasNumber = True
    try:
        for character in value:
            if ord(character) >= 48 and ord(character) <= 57:
                pass
            else:
                ifHasNumber = False
        if ifHasNumber:
            return ifHasNumber
    except:
        pass
    print("{:d}".format(value))
    return ifHasNumber

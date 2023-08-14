#!/usr/bin/python3
def no_c(my_string):
    str_new = ""
    for chars in my_string:
        if chars != 'c' and chars != 'C':
            str_new += chars
    return str_new

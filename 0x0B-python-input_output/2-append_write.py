#!/usr/bin/python3
"""write to a file"""


def append_write(filename="", text=""):
    """write to file
    Arg:
        filename: name of the file
        text: text to be written
    Return:
        int: number of characters written
    """
    with open(filename, "a") as file:
        file.write(text)
    return len(text)

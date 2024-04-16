#!/usr/bin/python3
"""write to a file"""


def write_file(filename="", text=""):
    """write to file
    Arg:
        filename: name of the file
        text: text to be written
    Return:
        int: number of characters written
    """
    with open(filename, "w") as file:
        file.write(text)
    return len(text)

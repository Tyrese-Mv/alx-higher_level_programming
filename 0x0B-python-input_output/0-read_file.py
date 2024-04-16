#!/usr/bin/python3
"""Read FIle"""


def read_file(filename=""):
    """reads file
    Arg:
        filename: name of the file
    """
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            print(line, end="")

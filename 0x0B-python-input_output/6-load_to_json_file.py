#!/usr/bin/python3
"""To JSON string"""


import json


def load_from_json_file(filename):
    """converter
    Arg:
        filename: name of the file
    """
    with open(filename, encoding='utf-8') as file:
        content = json.load(file)
        return content

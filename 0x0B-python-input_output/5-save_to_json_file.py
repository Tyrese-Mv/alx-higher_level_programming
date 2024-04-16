#!/usr/bin/python3
"""To JSON string"""


import json


def save_to_json_file(my_obj, filename):
    """converter
    Arg:
        my_obj: object
        filename: name of the file
    """
    with open(filename, "w", encoding='utf-8') as file:
        content = json.dumps(my_obj)
        file.write(content)

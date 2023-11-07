#!/usr/bin/python3
"""To JSON string"""


import json


def from_json_string(my_str):
    """converter
    Arg:
        my_str: string
    """
    return json.loads(my_str)

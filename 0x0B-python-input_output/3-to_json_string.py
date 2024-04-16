#!/usr/bin/python3
"""To JSON string"""


import json


def to_json_string(my_obj):
    """converter
    Arg:
        my_obj: object
    """
    return json.dumps(my_obj)

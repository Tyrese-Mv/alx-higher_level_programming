#!/usr/bin/python3
"""task 7"""


import os.path
import sys
import json

if __name__ == "__main__":
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = __import__("5-load_from_json_file").load_from_json_file


    arguments = []
    if os.path.exists('add_item.json') and os.path.getsize('add_item.json') != 0:
        arguments = load_from_json_file('add_item.json')

    if len(sys.argv) > 1:
        for idx in range(1, len(sys.argv):
                arguments.append(str(sys.argv[idx]))

    save_to_json_file(arguments, 'add_item.json')

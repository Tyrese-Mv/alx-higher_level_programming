#!/usr/bin/python3
"""task 7"""


import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def add_items_to_list(arguments):
    new_list = load_from_json_file('add_item.json') or []

    new_list.extend(arguments)

    save_to_json_file(new_list, 'add_item.json')

if __name__ == "__main__":
    arguments = sys.argv[1:]

    if arguments:
        add_items_to_list(arguments)

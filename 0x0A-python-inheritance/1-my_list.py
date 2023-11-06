#!/usr/bin/python3
"""Inherits from list"""
class MyList(list):
    """instantiate using a super class"""
    def __init__(self):
        super().__init__()
    def print_sorted(self):
        """sorts a list in ascending order"""
        self.sort()
        print(self)


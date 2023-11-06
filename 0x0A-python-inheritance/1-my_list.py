#!/usr/bin/python3
"""Inherits from list"""
class MyList(list):
    def print_sorted(self):
        """sorts a list in ascending order"""
        self.sort()
        print(self)


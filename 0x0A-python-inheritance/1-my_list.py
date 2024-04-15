#!/usr/bin/python3

"""Inherits fiom list"""


class MyList(list):

    """sorts a list in ascending order"""

    def print_sorted(self):
        self.sort()
        print(self)

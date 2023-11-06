#!/usr/bin/python3
"""My Int"""


class MyInt(int):
    """My Int"""

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)

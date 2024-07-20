#!/usr/bin/python3
"""Technical interview preparation:"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): list of integers

    Returns:
        int: largest number
    """
    if list_of_integers is None:
        return None
    return max(list_of_integers)

#!/usr/bin/python3
"""Module for defining MyList class"""


class MyList(list):
    """A subclass of the built-in list that can print itself sorted."""

    def print_sorted(self):
        """Print the list elements in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)

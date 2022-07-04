#!/usr/bin/python3
# 1-my_list.py
"""Defines an inherited list class MyList."""

class MyList(list):
    """A class MyList that inherits from list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))

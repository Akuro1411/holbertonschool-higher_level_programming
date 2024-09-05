#!/usr/bin/python3
"""
MyList class is inherited from built-in class.
"""


class MyList(list):
    """
    Makes the list object
    """
    def print_sorted(self):
        """
        Prints the sorted variant of itself
        """
        print(sorted(self))

#!/usr/bin/env python3
"""No module is imported"""


class VerboseList(list):
    """Inherits the class from the list class"""
    def append(self, __object):
        """Appends the element to end of the list"""
        self += [__object]
        print(f"Added [{__object}] to the list.")

    def extend(self, __iterable):
        """Appends list of elements to end"""
        n = len(__iterable)
        self += __iterable
        print(f"Extended the list with [{n}] items.")

    def pop(self, __index=-1):
        """Pops the element for given index(default = -1)"""
        number = self[__index]
        del self[__index]
        print(f"Popped [{number}] from the list.")

    def remove(self, __value):
        """Removes the element which is equal to value"""
        for i in range(len(self)):
            if self[i] == __value:
                break
        del self[i]
        print(f"Removed [{__value}] from the list.")

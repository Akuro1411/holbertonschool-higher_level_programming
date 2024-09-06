#!/usr/bin/python3
"""No module is imported for understanding of multiple inheritance in python's classes"""

class Fish:
    """Defines the fish"""
    def swim(self):
        """Prints the swimming skill of fish"""
        print("The fish is swimming")

    def habitat(self):
        """The living place of fish"""
        print("The fish lives in water")


class Bird:
    """Defines the bird"""
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        """The living place of bird"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """This class implemented with multiple inheritance"""
    def fly(self):
        """Flying fish what???"""
        print("The flying fish is soaring!")

    def swim(self):
        """Swimming is normal feature of fish"""
        print("The flying fish is swimming!")

    def habitat(self):
        """How can fish live in water and the sky???"""
        print("The flying fish lives both in water and the sky!")

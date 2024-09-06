#!/usr/bin/python3
"""No module is imported. Main point: Mixins in python"""


class SwimMixin:
    """The class can perform only one method not complex initializations or methods"""
    def swim(self):
        """The swim method is portable across classes"""
        print("The creature swims!")


class FlyMixin:
    """The class can perform only one method not complex initializations or methods"""
    def fly(self):
        """The fly method is portable across classes"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """You can define dragon object with this class"""
    def roar(self):
        """A dragon can roar"""
        print("The dragon roars!")

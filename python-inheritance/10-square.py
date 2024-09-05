#!/usr/bin/python3
"""
No module is imported.Class for Geometry
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square object that parent class is Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(width=size, height=size)
        self.__size = size

    def area(self):
        """
        :return: The area of square
        """
        return self.__size ** 2

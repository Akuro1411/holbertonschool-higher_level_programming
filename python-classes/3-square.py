#!/usr/bin/python3
"""Make a class Square."""


class Square:
    """The square class for square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        There is no argument for this method
        :return: Returns the area of square
        """
        area = pow(self.__size, 2)
        return area

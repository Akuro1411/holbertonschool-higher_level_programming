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

    @property
    def size(self):
        """
        :return: Returns the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        :param value: The new size of the square
        :return: Nothing is returned by function
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        :return: No return, prints the square of #
        """
        edge = self.__size
        if edge == 0:
            print("")
        for i in range(edge):
            for j in range(edge):
                print("#", end="")
            print()

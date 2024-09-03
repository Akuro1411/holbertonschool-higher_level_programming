#!/usr/bin/python3
"""Make a class Square."""


class Square:
    """The square class for square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (not isinstance(position[0], int)) or (not isinstance(position[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")        
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        :return: The position of square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        :param value:
        :return: Returns nothing because it is setter
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        :return: No return, prints the square of #
        """
        edge = self.__size
        spaces = self.__position[0]
        if edge == 0:
            print("")
        for i in range(edge):
            if self.__position[1] == 0:
                for t in range(spaces):
                    print(" ", end="")
            for j in range(edge):
                print("#", end="")
            print()

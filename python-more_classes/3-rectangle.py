#!/usr/bin/python3
"""
The rectangle class is implemented
"""


class Rectangle:
    """Instantiate the rectangle with width and height"""
    def __init__(self, width=0, height=0):
        """
        :param width: Sets the number for width
        :param height: Sets the number for height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        :return: Returns the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        :param value:
        :return: Returns nothing
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        :return: Returns the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        :param value:
        :return: Returns nothing
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        :return: Returns the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        :return: Returns the perimetr of the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__height * 2 + self.__width * 2

    def __str__(self):
        string = ""
        if self.__height == 0 or self.__width == 0:
            return string
        for i in range(self.__height):
            for j in range(self.__width):
                string += "#"
            if i != self.__height - 1:
                string += "\n"
        return string

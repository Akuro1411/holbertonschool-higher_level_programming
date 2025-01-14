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

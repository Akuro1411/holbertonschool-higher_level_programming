#!/usr/bin/python3
"""
No module is imported.Class for Geometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class is derived from BaseGeometry
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        :return: The area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] %d/%d" % (self.__width, self.__height)

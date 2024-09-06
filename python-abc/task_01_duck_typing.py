#!/usr/bin/env python3
"""
abs module is imported for abstraction
Math module is imported for pi
"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Base class for all figures"""
    @abstractmethod
    def area(self):
        """Blueprint method for figures"""
        pass

    @abstractmethod
    def perimeter(self):
        """Blueprint method for figures"""
        pass


class Circle(Shape):
    """The circle class takes radius as an argument"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        :return: Returns the area of the circle
        """
        return pi * (self.radius ** 2)

    def perimeter(self):
        """
        :return: Returns the perimeter of the circle
        """
        return 2 * pi * self.radius


class Rectangle(Shape):
    """The rectangle class takes width and height of rectangle as arguments"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """
        :return: Returns the area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        :return: Returns the perimeter of the rectangle
        """
        return (self.width + self.height) * 2


def shape_info(obj):
    """Prints the area and perimeter of the given object
       This function implemented for duck typing
    """
    area = obj.area()
    perimeter = obj.perimeter()
    print(f"Area: {area}")
    print(f"Perimetr: {perimeter}")

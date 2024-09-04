#!/usr/bin/python3
"""
The rectangle class is implemented
"""


class Rectangle:
    """Instantiate the rectangle with width and height"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        :param width: Sets the number for width
        :param height: Sets the number for height
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1
        self.print_symbol = Rectangle.print_symbol
        # self.__class__.number_of_instances += 1
        # Both of them are same thing.
        # But the upper one won't work with old style class instances
        # Because their type is not class (their type is instance)

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
        if Rectangle.print_symbol != "#":
            if self.print_symbol == "#":
                self.print_symbol = Rectangle.print_symbol
        if self.__height == 0 or self.__width == 0:
            return string
        for i in range(self.__height):
            for j in range(self.__width):
                string += str(self.print_symbol)
            if i != self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        return "Rectangle(2, 4)"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        # You can also access the class variable through the class name
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        :param rect_1:
        :param rect_2:
        :return: Returns the biggest rectangle based on area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        first_area = Rectangle.area(rect_1)
        second_area = Rectangle.area(rect_2)
        if first_area < second_area:
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """
        :param size:
        :return: Returns the square with given size
        """
        return cls(size, size)

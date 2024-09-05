#!/usr/bin/python3
"""
No module is imported.Class for Geometry
"""


class BaseGeometry:
    """BaseGeometry class for geometry"""
    def area(self):
        """
        :raise: Raises an exception for undefined area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        :param name:
        :param value:
        :return: Checks for the value is integer or not
        """
        if type(value) is not int:
            raise TypeError("{name} must be an integer".format(name=name))
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")

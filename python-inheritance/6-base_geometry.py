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

#!/usr/bin/python3
"""
Contains the inherits_from function
"""


class BaseGeometry:
    """A class with public attribute area"""
    def area(self):
        """
        Calculates the area of the geometry.
        """
        raise Exception("area() is not implemented")

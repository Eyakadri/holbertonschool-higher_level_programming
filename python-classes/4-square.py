#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines properties of square

    Attributes:
        size: size of a square
    """

    def __init__(self, size=0):
        """
        Creates new instances of square

        Args:
            size: size of the square
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2

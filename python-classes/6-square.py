#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines properties of square

    Attributes:
        size: size of a square
        position: tuple representing the position to start printing
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Creates new instances of square

        Args:
            size: size of the square
            position: tuple representing the position to start printing
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(i, int) for i in value)
        ):
            raise TypeError("position must be a tuple of two positive integers")
        else:
            self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()

            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size, end="")
                if i < self.__size - 1:
                    print()

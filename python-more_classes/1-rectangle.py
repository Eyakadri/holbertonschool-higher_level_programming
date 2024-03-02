#!/usr/bin/python3


class Rectangle:
    def __init__(self, width=0, height=0):
        # Initialize Rectangle instance with default width and height
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        # Setter method for the width attribute
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        # Getter method for the height attribute
        return self.__height

    @height.setter
    def height(self, value):
        # Setter method for the height attribute
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

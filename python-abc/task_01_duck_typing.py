#!/usr/bin/env python3

from abc import ABC, abstractmethod
import math


class Shape(ABC):  # Abstract class Shape
    @abstractmethod
    def area(self):
        pass    # Abstract method for calculating area

    @abstractmethod
    def perimeter(self):
        pass    # Abstract method for calculating perimeter


class Circle(Shape):  # Circle class inherits from Shape
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):  # Rectangle class inherits from Shape
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


def perimeter(self):
    return 2 * (self.width + self.height)


def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

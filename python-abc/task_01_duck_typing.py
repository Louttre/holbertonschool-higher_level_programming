#!/usr/bin/env python3
"""
This shebang line ensures the script runs with Python 3 interpreter.
"""

from abc import ABC, abstractmethod
# Importing ABC and abstractmethod from the ABC module.

import math
# Importing the math module for mathematical operations.


class Shape(ABC):
    """
    Abstract base class for shapes.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Circle class inheriting from Shape.
    """

    def __init__(self, radius):
        """
        Constructor for Circle class.
        """
        self.radius = abs(radius)

    def area(self):
        """
        Calculate the area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle.
        """
        return self.radius * 2 * math.pi


class Rectangle(Shape):
    """
    Rectangle class inheriting from Shape.
    """

    def __init__(self, width, height):
        """
        Constructor for Rectangle class.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        """
        return (self.width + self.height) * 2


def shape_info(shape):
    """
    Function to print the area and perimeter of a shape.
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())

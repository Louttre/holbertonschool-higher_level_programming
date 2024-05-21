#!/usr/bin/python3
"""Class definition for BaseGeometry"""


class BaseGeometry:
    """This class serves as a base for geometry-related classes"""

    def area(self):
        """Placeholder method for calculating the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a value is an integer greater than 0.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Method for calculating the area"""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

class Square(Rectangle):

    def __init__(self, size):
                """Initialize a new Rectangle instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Method for calculating the area"""
        return self.__size * self.__size

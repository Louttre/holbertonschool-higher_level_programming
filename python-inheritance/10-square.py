#!/usr/bin/python3
"""Class definition for BaseGeometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square, inheriting from BaseGeometry."""

    def __init__(self, size):
        """Initialize a new Rectangle instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Method for calculating the area"""
        return self.__size * self.__size

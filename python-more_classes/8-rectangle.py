#!/usr/bin/python3
"""Module for defining a rectangle class"""


class Rectangle:
    """A class representing rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle."""

        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
            If width or height is 0, returns 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def print(self):
        """Print the rectangle using the '#' character."""

        i = 0
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height):
            print(str(self.print_symbol) * self.__width)

    def __str__(self):
        """Return a string representation of the rectangle."""

        if self.__height == 0 or self.__width == 0:
            return ""
        rect_lines = []
        for _ in range(self.__height):
            rect_lines.append(str(self.print_symbol) * self.__width)
        return "\n".join(rect_lines)

    def __repr__(self):
        """Return a string that can recreate the object using interpreter."""

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when an instance is deleted"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles and returns the one with greater area.

        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.

        Returns:
            Rectangle: The rectangle with equal or greater area.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

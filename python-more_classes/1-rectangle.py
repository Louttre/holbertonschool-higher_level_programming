#!/usr/bin/python3
'''Module for defining a rectangle class'''


class Rectangle:
    """A class representing rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance.
        
        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        
        return self.__width

    @width.setter
    """Set the width of the rectangle.
        
    Args:
        value (int): The new width value.
        
    Raises:
        TypeError: If the width is not an integer.
        ValueError: If the width is less than 0.
    """    
    
    def width(self, value):
        if not isinstance(value, int)
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value

    @property
    """Get the height of the rectangle."""
    
    def height(self):
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
        
        if not isinstance(value, int)
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

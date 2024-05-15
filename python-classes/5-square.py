#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """A class representing a square."""
    def __init__(self, size=0):
        """Initialize a square with the given size.

        Args:
            size (int, optional): The size of each side of the square.
                Defaults to 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print('#', end='')
                for j in range(self.__size):
                    print('#', end='')
                print()

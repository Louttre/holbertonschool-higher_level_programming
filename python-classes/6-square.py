
#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """A class representing a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with the given size and position.

        Args:
            size (int, optional): The size of each side of the square.
                Defaults to 0.
            position (tuple, optional): The position of the square.
                Defaults to (0, 0).
        Raises:
            TypeError: If size is not an integer or if position is not a tuple
                      of two positive integers.
            ValueError: If size is less than 0 or if position contains negative
                        values.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if not isinstance(position, tuple) or len(position) != 2 \
                or not all(isinstance(coord, int) for coord in position) \
                or not all(coord >= 0 for coord in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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
        
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The new position of the square.
        Raises:
            TypeError: If value is not a tuple of two positive integers.
            ValueError: If value contains negative values.
        """
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(coord, int) for coord in value) \
                or not all(coord >= 0 for coord in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
        
    
    def my_print(self):
        """Print the square using hash symbols.

        If the size of the square is 0, print an empty line.
        Otherwise, print a square shape using hash symbols.
        """
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for j in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
    

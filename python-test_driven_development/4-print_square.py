#!/usr/bin/python3

def print_square(size):

    if not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")    
    for i in range(self.__size):
        print('#', end='')
        for j in range(self.__size - 1):
            print('#', end='')
        print()               

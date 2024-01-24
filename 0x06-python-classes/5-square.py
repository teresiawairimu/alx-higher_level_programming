#!/usr/bin/python3
"""A module that defines a square based on task 4
Attributes:
    __size: size of the square
Todo:
    Public instance method: def my_print(self): that prints in stdout the square
    if size is equal to 0, print an empty line
"""
class Square:
    """A class that represents a Square."""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
    @property
    def size(self):
        """Getter for the size attribute"""
        return self.__size
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def area(self):
        """Calculates the area of the square
        Returns:
                int: Area of the square
        """                         
        return self.__size ** 2
    def my_print(self):
        if self.__size == 0:
            print('')
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

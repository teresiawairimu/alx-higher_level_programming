#!/usr/bin/python3
"""A module that defines a square based on task 2

Attributes:
    __size: size of the square
Todo:
    property def size(self): to retrieve it
    property setter def size(self, value): to set it
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

#!/usr/bin/python3
"""A module that defines a square based on task 1.

Attributes:
    __size: size of the square
Todo:
    Private instance attribute: size
    instantiation with optional size: def __init__(self, size=0)
    size must be an integer, otherwise raise a TypeError exception
    if size is less than 0, raise a ValueError exception
"""
class Square:
    """Represents a Square"""
    def __init__(self, size=0):
        """Constructor of the Square class.

        Args:
            size: size of the square
        """
        if type(size) != int:
            raise TypeError('size must be an integer')
        else:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size


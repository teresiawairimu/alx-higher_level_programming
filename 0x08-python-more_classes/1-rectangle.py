#!/usr/bin/path
"""A class that defines a rectangle
"""


class Rectangle:
    """Represents a rectangle

    Attributes:
        __width: The width of the rectangle
        __height: The height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """Constructor of the rectangle instance

        Args:
            width: The width of the rectangle
            height: The height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """retrieves width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """The setter method"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """The getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """The setter method"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value

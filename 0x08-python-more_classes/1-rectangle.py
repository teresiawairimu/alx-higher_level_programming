#!/usr/bin/path
"""A class that defines a rectangle"""


class Rectangle:
    """Represents a rectangle

    Attributes:
        __width: The width of the rectangle
        __height: The height of the rectangle
    """

    def __init__(self, height=0, width=0):
        """Constructor of the rectangle instance

        Args:
            width: The width of the rectangle
            height: The height of the rectangle
        """
        self.height = height
        self.width = width

    @property
    """The getter method"""
    def height(self):
        return self.__height

    @height.setter
    """The setter method"""
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    """The getter method"""
    def width(self):
        return self.__width

    @width.setter
    """The setter method"""
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

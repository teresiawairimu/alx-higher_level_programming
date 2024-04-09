#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """Represents a rectangle

    Attributes:
        __width: The width of the rectangle
        __height: the height of the triangle
    """

    def __init__(self, width=0, height=0):
        """Constructor for the rectangle instance

        Args:
            width (int): The width of the rectangle (default 0)
            height (int): The height of the rectangle (default 0)
        """
        self.__width = width
        self.__height = height

    def width(self):
        """The getter method for the width"""
        return self.__width

    def width(self, value):
        """The setter method for the width"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    def height(self):
        """The getter method for the height"""
        return self__height

    def height(self, value):
        """The setter method for the height"""
        if isinstance(value, int):
            if height < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")

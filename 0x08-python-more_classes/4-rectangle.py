#!/usr/bin/python3
"""A class for working with rectangles.
"""


class Rectangle:
    """Represents a rectangle
    """
    def __init__(self, width=0, height=0):
        """Initializes the instancce of the Rectangle class.

        Args:
            width: The width of the rectangle
            height: The height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle
        """
        return self.__width

    @property
    def height(self):
        """Retrieves the height of the rectangle
        """
        return self.__height

    @width.setter
    def width(self):
        """sets the width of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """sets the height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Computes the area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """Computes the perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """returns a string representation of the object
        """
        if self.width == 0 or self.height == 0:
             return ''
        rectangle = ''
        for _ in range(self.height):
            rectangle += '#' * self.width + '\n'
        return rectangle.rstrip('\n')
    def __repr__(self):
        """returns a string representation of the object
        """
        return 'Rectangle({:d}, {:d})'.format(self.width, self.height)


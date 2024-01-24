#!/usr/bin/python3
"""A module that creates a square"""

class Square:
    """A class that defines a square.

    Attributes:
        size(int): size of the square
        position(tuple): position use by using space
    """
    def __init__(self, size=0, position=(0, 0)):
        """Constructor for the class
        Args:
            size(int): size of the square
            position(tuple): position
        Returns:
            None
        """
        self.size = size
        self.position = position

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
    @property
    def position(self):
        """get attribute called position
        set position 
        Args:
            value(tuple): position of the square
        """
        return self.__position
    
    @position.setter
    def position(self, value):
        if len(value) != 2 or type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                    print(" " * self.__position[0] + "#" * self.__size)


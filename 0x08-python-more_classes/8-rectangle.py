#!/usr/bin/python3
"""
Rectangle Module
"""


class Rectangle:
    """
    Write an empty class Rectangle that defines a rectangle:

    Args:
        width (int): int
        height (int): int

    Attributes:
        width (int): int
        height (int): int
        number_of_instances (int): number of Rectangles
        print_symbol: symbol

    Raises:
        TypeError: not an integer
        ValueError: less than 0
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """int: width"""
        return self.__width

    @property
    def height(self):
        """int: height"""
        return self.__height

    @height.setter
    def height(self, value):
        """


#!/usr/bin/python3
"""
Module containing the Rectangle class.
"""
class Rectangle:
    """
    Defines a rectangle.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    def get_width(self):
        return self.__width
    def set_width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    def get_height(self):
        return self.__height
    def set_height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
    def area(self):
        return self.__width * self.__height
    def perimeter(self):
        return 2 * (self.__width + self.__height)

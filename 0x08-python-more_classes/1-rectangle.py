#!/usr/bin/python3

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

if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print(my_rectangle.__dict__)

    my_rectangle.set_width(10)
    my_rectangle.set_height(3)
    print(my_rectangle.__dict__)


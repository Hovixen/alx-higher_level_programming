#!/usr/bin/python3
""" rectangle class """


class Rectangle:
    """
       Rectangle class that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """ Method initializes class attributes """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter method to return the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter method to set the width value of an object """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")

        else:
            self.__width = value

    @property
    def height(self):
        """ getter method to return the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter method to set the height value of an object """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")

        else:
            self.__height = value

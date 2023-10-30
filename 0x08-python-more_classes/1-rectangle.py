#!/usr/bin/python3
""" rectangle class """


class Rectangle:
    """
       Rectangle class that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """ Method initializes class attributes """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ getter method to return the width """
        return self.__width

    @width.setter
    def width(self, obj_val):
        """ setter method to set the width value of an object """
        if not isinstance(obj_val, int):
            raise TypeError("width must be an integer")

        elif obj_val < 0:
            raise ValueError("width must be >= 0")

        else:
            self.__width = obj_val

    @property
    def height(self):
        """ getter method to return the height """
        return self.__height

    @height.setter
    def height(self, obj_val):
        """ setter method to set the height value of an object """
        if not isinstance(obj_val, int):
            raise TypeError("height must be an integer")

        elif obj_val < 0:
            raise ValueError("height must be >= 0")

        else:
            self.__height = obj_val

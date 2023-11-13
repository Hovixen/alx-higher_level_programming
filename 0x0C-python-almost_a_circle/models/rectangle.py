#!/usr/bin/python3
""" This module is a rectangle subclass """
from models.base import Base


class Rectangle(Base):
    """ A rectangle subclass that inherits from the Base """


    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes the new instances for the rectangle class """
        
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Getter method for width attribute """
        return self.__width
    @width.setter
    def width(self, val):
        """ Setter method for the width attribute """
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        elif val < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = val

    @property
    def height(self):
        """ Getter method for height attribute """
        return self.__height
    @height.setter
    def height(self, val):
        """ Setter method for the height attribute """
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        elif val < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = val

    @property
    def x(self):
        """ Getter method for x attribute """
        return self.__x
    @x.setter
    def x(self, val):
        """ Setter method for the x attribute """
        if not isinstance(val, int):
            raise TypeError("x must be an integer")
        elif val < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = val

    @property
    def y(self):
        """ Getter method for the y attribute """
        return self.__y
    @y.setter
    def y(self, val):
        """ Setter method for the y attribute """
        if not isinstance(val, int):
            raise TypeError("y must be an integer")
        elif val < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = val

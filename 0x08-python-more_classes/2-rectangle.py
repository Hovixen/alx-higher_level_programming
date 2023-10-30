#!/usr/bin/python3
""" Class that defines a rectangle """


class Rectangle:
    """ Class defines a area and perimeter of a rectangle """
    def __init__(self, width=0, height=0):
        """ Method initializes the instances

        Arguments:

            width: optional parameter width of rectangle
            height: optional parameter height of rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter method that  gets width value of rectangle

        Returns width of rectangle

        """

        return self.__width

    @width.setter
    def width(self, value):
        """ Setter method that sets width value of rectangle

        Arguments:

            value: value parameter to set to width

        Raises:

            TypeError: when value is not an integer
            ValueError: when value is negative

        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")

        else:
            self.__width = value

    @property
    def height(self):
        """ Getter method that gets height value of rectangle

        Returns height of rectangle

        """

        return self.__height

    @height.setter
    def height(self, value):
        """ Setter method that sets height value of rectangle

        Arguments:

            value: value parameter to set to height

        Raises:

            TypeError: when value is not an integer
            ValueError: when value is negative

        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")

        else:
            self.__height = value

    def area(self):
        """ Method finds the area of rectangle """

        return self.__width * self.__height

    def perimeter(self):
        """ Method finds the perimeter of rectangle """

        return ((self.__width + self.__height) * 2)

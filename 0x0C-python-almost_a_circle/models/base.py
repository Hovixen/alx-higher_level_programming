#!/usr/bin/python3
""" This model contains the Base Class """


class Base:
    """ Base class that manages id attributes in all
        future class instances created """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializing the Base class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            # assiging the new value of count to the id
            self.id = Base.__nb_objects

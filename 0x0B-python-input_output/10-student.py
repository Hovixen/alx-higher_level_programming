#!/usr/bin/python3
""" Module that defines the class Student
"""


class Student:
    """ Class to create student instances """

    def __init__(self, first_name, last_name, age):
        """ Special method to initialize """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Method that returns directory description """

        if attrs == None:
            return self.__dict__.copy()
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

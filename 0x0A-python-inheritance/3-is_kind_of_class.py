#!/usr/bin/python3
"""
task 3 function checks if an object is an instance of a class
"""


def is_kind_of_class(obj, a_class):
    """
    function returns True if the object is an instance of the specified class
    otherwise False

    Args:
        obj(object): object to be passed and checked
        a_class (type): class to compare the object to

    Return:
        bool: True if the object is an instance of the class or
            False if not                              """

    return isinstance(obj, a_class)

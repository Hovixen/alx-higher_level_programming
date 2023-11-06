#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    function returns True if the object is exactly
    an instance of the specified class; otherwise False

    Args:
        obj(object): object to be passed and checked
        a_class (type): class to compare the object to

    Return:
        bool: True if the object is an instance of the class or
            False if not
    """

    return isinstance(obj, a_class)

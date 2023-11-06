#!/usr/bin/python3

"""
function returns list of available attributes and methods of an object
"""


def lookup(obj):
    """
    Args:
        obj: object or class that is passed to the function

    Return:
    List: returns a list of attributes and methods of the class passed
    """

    return [at for at in dir(obj)]

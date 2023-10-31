#!/usr/bin/python3
"""


    This class prevents the user from dynamically creating
    new instance attributes, except if new instance attribute
    is called first_name

"""
class LockedClass:
    """ Class module """
    __slots__ = ("first_name")

    def __init__(self):
        """ Method initializes the instance """
        pass

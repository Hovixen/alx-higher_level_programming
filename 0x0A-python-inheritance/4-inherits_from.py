#!/usr/bin/python3
"""
function check an instance of a class that inherited (directly or indirectly)
from the specified class
"""


def inherits_from(obj, a_class):
    """
    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a class that inherited from a_class;
        False otherwise.
    """
    return isinstance(obj, a_class) and obj.__class__ != a_class

#!/usr/bin/python3
"""Check if the given object is an instance of a class inherited
(directly or indirectly) from a_class.
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
    if not isinstance(obj, type):
        return False
    return issubclass(type(obj), a_class)

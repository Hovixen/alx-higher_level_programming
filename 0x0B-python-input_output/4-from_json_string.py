#!/usr/bin/python3
""" Module that contains a function that returns an object by
a JSON representation
"""
import json


def from_json_string(my_str):
    """ Function that returns an object by a JSON representation

    Args:
        my_str: JSON representation

    Raises:
        Exception: when the string can't be decoded

    """
    my_str_obj = json.loads(my_str)
    return my_str_obj

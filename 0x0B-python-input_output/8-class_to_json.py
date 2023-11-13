#!/usr/bin/python3
""" Module that returns the dictionary description with a simple
data structure for a JSON serialization of an object
"""


def class_to_json(obj):
    """ Function that retuns the dictionary description of an obj """

    # get the copy of the object attributes

    obj_attr = obj.__dict__.copy()

    # create an empty sterilized dictionary

    dic = {}
    for key, value in obj_attr.items():
        if isinstance(value, (list, dict, str, int, bool)):
            dic[key] = value
    return dic


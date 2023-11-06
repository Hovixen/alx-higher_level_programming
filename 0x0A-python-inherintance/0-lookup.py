#!/usr/bin/python3

def lookup(obj):
    # function returns list of available attributes and methods of an object

    return [at for at in dir(obj)]

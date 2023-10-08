#!/usr/bin/python3

def multiple_returns(sentence):
    # this function returns a tuple with the length of a string
    # and its first character
    if len(sentence) == 0:
        tuples = (len(sentence), None)
    else:
        tuples = (len(sentence), sentence[0])
    return tuples

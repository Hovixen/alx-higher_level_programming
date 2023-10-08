#!/usr/bin/python3

def multiple_returns(sentence):
    # this function returns a tuple with the length of a string
    # and its first character
    if len(sentence) == 0:
        char1 = None
    else:
        return (len(sentence), sentence[0])

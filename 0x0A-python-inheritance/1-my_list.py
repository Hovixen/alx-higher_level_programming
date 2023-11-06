#!/usr/bin/python3
"""
class that inherits from in-built function
"""


class MyList(list):
    """
    This class MyList is a child class of the in-built function list
    and it has a public method that prints the list in sorted order (ascending)
    """

    def print_sorted(self):
        """
        This function sorts the list in ascending order
        """
        sortedList = sorted(self)
        listElements = []
        for elements in sortedList:
            listElements.append(elements)
        print(listElements)

#!/usr/bin/python3

class MyList(list):
    """Inherits from list and provides a method to print the list sorted."""

    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)

#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        """
contains the MyList class
"""

        sorted_list = sorted(self)
        print(sorted_list)

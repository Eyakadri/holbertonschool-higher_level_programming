#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        """
        Prints the list sorted in ascending order.

        Parameters:
            None

        Returns:
            None
        """
        sorted_list = sorted(self)
        print(sorted_list)

#!/usr/bin/python3
"""module containing the function read_file"""


def read_file(filename=""):
    """reads a file and prints to stdout    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')

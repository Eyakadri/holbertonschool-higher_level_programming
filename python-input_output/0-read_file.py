#!/usr/bin/python3
"""function containing the function read_file
"""


def read_file(filename=""):
    """ reads a text file
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

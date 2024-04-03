#!/usr/bin/python3
"""
 a function that appends a string at the end of a text file (UTF8)
"""


def append_write(filename="", text=""):
    """Appends a string to a text file (UTF8)    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)

#!/usr/bin/python3
def raise_exception():
    try:
        raise TypeError("Custom type exception raised")
    except TypeError as a:
        raise a

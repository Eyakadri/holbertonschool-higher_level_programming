#!/usr/bin/python3
"""
Contains the inherits_from function.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class.
    Parameters:
    obj: The object to check.
    a_class: The class to check against.
    Returns:
    bool: True if obj is a subclass of a_class, otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class

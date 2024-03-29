#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    
    Parameters:
        obj: Any Python object
    
    Returns:
        list: List of available attributes and methods
    """
    return dir(obj)

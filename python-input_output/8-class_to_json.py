#!/usr/bin/python3
"""a function that returns the dictionary description"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure"""
    serializable_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_dict[key] = value
    return serializable_dict

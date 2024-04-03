#!/usr/bin/python3
"""module containing the function from_json_string"""
import json


def from_json_string(my_str):
    """returns an object
    """
    return json.loads(my_str)

#!/usr/bin/python3
"""Module containing the function save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file using JSON representation
    """

    with open(filename, 'w', encoding="utf-8") as f:
        json_object = json.dumps(my_obj)
        f.write(json_object)
        f.close()

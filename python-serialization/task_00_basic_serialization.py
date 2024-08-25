#!/usr/bin/env python3

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary
    :parameter data: Dictionary to serialize
    :parameter filename: Name of the file
    """
    try:
        with open(filename, 'w') as json_file:
            json.dump(data, json_file)
    except Exception as e:
        print(f"An error occurred while serializing and saving to file: {e}")


def load_and_deserialize(filename):
    """
    Loads a JSON file and deserializes
    :parameter filename: Name of the JSON file to read
    :return: Dictionary deserialized
    """
    try:
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
        return data
    except Exception as e:
        print(f"An error occurred while loading: {e}")
        return None
